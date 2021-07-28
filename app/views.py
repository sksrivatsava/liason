from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import CustomUser,Post
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

def page0_base(request):
    present_user = str(request.user)
    user=CustomUser.objects.get(userid=request.user)
    print(user.acctype)
    return render(request,'page0_base.html',context={'present_user':present_user,'u':user})

#this page displays all posts
#for now, we create a post from this page
@login_required(login_url='http://127.0.0.1:8000/page4_login/')
def page1_home(request):
    user= CustomUser.objects.get(userid=request.user)
    present_user = str(request.user)
    #print(present_user)
    print(len(user.foll_req.split()))
    l=[]
    l1=[]
    l2=[]
    f=user.foll.split()
    list_temp = Post.objects.order_by('-date')
    for i in list_temp:
        if i.userid in f:
            l.append(i)
            l1.append(CustomUser.objects.get(userid=i.userid))
    l2=zip(l,l1)

    return render(request,'page1_home.html',{'l': l2,'present_user':present_user,'u':user})


#this page shows your friends and people you may want to follow
#a search engine will redirect to this
def page2_friends(request):
    present_user = str(request.user)
    user=CustomUser.objects.get(userid=request.user)
    if request.method=='POST':
        a = request.POST['name_search']
        b = request.POST['department_search']
        c = request.POST['designation_search']
        l3 = CustomUser.objects.filter((Q(username__icontains=a)|Q(userid__icontains=a))&Q(designation__icontains=c)&Q(department__icontains=b))
        flag = 1
        
    else:
        pu = CustomUser.objects.get(userid=request.user).department
        l=CustomUser.objects.filter(department=pu)
        a=CustomUser.objects.get(userid=request.user)
        l2=a.foll.split()
        l4=a.followers.split()
        flag = 0
        l3=[]
        for i in l:
            if i.userid not in l2 and i.userid != str(request.user):
                l3.append(i)
        if len(l3)==0:
            flag = 2
    return render(request,'page2_friends.html',context={'l3':l3,'present_user':present_user,'flag':flag,'u':user})
    

def page8_profile(request,fr):
    a=CustomUser.objects.get(userid=fr)
    l1 = a.foll.split()
    l1o = []
    for i in l1:
        l1o.append(CustomUser.objects.get(userid=i))
    l2=a.followers.split()
    l2o = []
    for i in l2:
        l2o.append(CustomUser.objects.get(userid=i))
    l3=Post.objects.order_by('-date').filter(userid=fr)
    present_user=str(request.user)
    user=CustomUser.objects.get(userid=request.user)
    ln1=len(l1)
    ln2=len(l2)
    ln3=len(l3)
    return render(request,'page8_profile.html',{'l1': l1o,'l2':l2o,'l3':l3,'p_user':fr,'present_user':present_user,'a':a,'ln1':ln1,'ln2':ln2,'ln3':ln3,'u':user}) 

    # l=CustomUser.objects.all()
    # a=CustomUser.objects.get(userid=request.user)
    # l2=a.foll.split()
    # l4=a.followers.split()
    # present_user = str(request.user)
    # return render(request,'page8_profile.html',context={'l2':l2,'l4':l4,'present_user':present_user})


def page5_following(request):
    nice = CustomUser.objects.get(userid=request.user)
    lis  = nice.foll.split()
    return render(request,'page5_following.html',context={'lis':lis})

def follow(request,fr):
    n = CustomUser.objects.get(userid=request.user)
    n.foll +=" "+fr
    n.save()
    n = CustomUser.objects.get(userid=fr)
    n.followers+=" "+str(request.user)
    n.save()
    
    return redirect('friends')

def logout(request):
    auth.logout(request)
    return redirect('login')
  
def follow_request(request,fr):
    n = CustomUser.objects.get(userid=fr)
    n.foll_req +=" "+str(request.user)
    n.save()

    return redirect('friends')

def accept_follow_request(request,fr):
    n = CustomUser.objects.get(userid=fr)
    n.foll += " "+str(request.user)
    n.save()
    n = CustomUser.objects.get(userid=request.user)
    n.followers += " "+fr
    n.save()
    n = CustomUser.objects.get(userid=request.user)
    n.foll_req=n.foll_req.replace(" "+fr,"")
    n.save()

    return redirect('follow_requests')

def reject_follow_request(request,fr):
    n = CustomUser.objects.get(userid=request.user)
    n.foll_req=n.foll_req.replace(" "+fr,"")
    print(n.foll_req)
    n.save()

    return redirect('follow_requests')

def unfollow(request,fr):
    n = CustomUser.objects.get(userid=request.user)
    n.foll = n.foll.replace(" "+fr,"")
    n.save()
    n = CustomUser.objects.get(userid=fr)
    n.followers = n.followers.replace(" "+str(request.user),"")
    n.save()

    return redirect('friends')



#this page is used for user registration
def page3_register(request):
    if request.method=='POST':
        if request.POST.get('init_pwd')== request.POST.get('conf_pwd'):
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request,'page3_register.html',{'error':'This username has already been taken.'})
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST['uname'],password = request.POST['init_pwd'])
                u1 = request.POST['uname']
                if ' ' in u1:
                    return render(request,'page3_register.html',{'error':'You are prohibited from using spaces in the username. Kindly check the same.'})
                u2 = request.POST['name']
                u3 = request.POST['department']
                u4 = request.POST['designation']
                u5 = request.POST['acctype']
                CustomUser.objects.get_or_create(userid=u1,username=u2,department=u3,designation=u4,acctype=u5)
                return render(request,'page4_login.html')
                # return HttpResponse("Signed Up!")
        else:
            return render(request,'page3_register.html',{'error':'Sorry, both the passwords do not match.'})
    else:
        return render(request,'page3_register.html')

def page4_login(request):
    
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['uname'],password=request.POST['pwd'])
        if user is not None:
            auth.login(request,user)
            return redirect('base')
            return HttpResponse("Logged in succesfully!")
        else:
            return render(request,'page4_login.html',{'error':'Invalid user credentials. Please check and try again.'})
    else:
        return render(request,'page4_login.html')
        
    
def page6_follow_requests(request):
    f = str(request.user)
    present_user = f

    n = CustomUser.objects.get(userid=request.user)
    lis = n.foll_req.split()    
    l3 = []
    for i in lis:
        l3.append(CustomUser.objects.get(userid=i))
        
    return render(request,'page6_follow_requests.html',context={'f':f,'l3':l3,'u':n,'present_user':present_user})

def page7_create_post(request):
    user=CustomUser.objects.get(userid=request.user)
    present_user=str(request.user)
    if request.method=='POST' or request.method=='FILES':
        u2 = request.POST['message']
        try:
            u3 = request.FILES['image']
            Post.objects.get_or_create(userid=str(request.user),message=u2,image=u3)
            return redirect('home')
        except:
            Post.objects.get_or_create(userid=str(request.user),message=u2)
            return redirect('home')
    else:
        return render(request,'page7_create_post.html',{'u':user,'present_user':present_user})
        
            
def upvote(request):
    print("upvote") 
    p_id= 0
    if request.method=='GET':
        p_id = request.GET['post_id']
    
 
    if p_id:
        post = Post.objects.get(id=int(p_id))
        if post:
            post.likediff=post.likediff+" "+str(request.user)
            post.likecount = len(post.likediff.split())
            post.save()

    print(p_id,post.likecount)      
    return HttpResponse(post.likecount)

# def like_count(request,id):
#     post=get_object_or_404(Post,id=request.POST.get('post_id'))

#     return HttpResponseRedirect(post.get_absolute_url())

def downvote(request):
    print("downvote")
    p_id= 0
    if request.method=='GET':
        p_id = request.GET['post_id']
    
 
    if p_id:
        post = Post.objects.get(id=int(p_id))
        if post:
            post.likediff=post.likediff.replace(" "+str(request.user),"")
            post.likecount = len(post.likediff.split())
            post.save()

    return HttpResponse(post.likecount)



def settings(request):
    present_user = str(request.user)
    u = CustomUser.objects.get(userid=present_user)
    return render(request,'settings.html',context = {'u':u,'present_user':present_user})

def change_username(request):
    if request.method=="POST":
        n = CustomUser.objects.get(userid=request.user)
        n.username=request.POST['uname']
        n.save()
        return redirect('settings')


# def change_profile_photo(request):
#     CustomUser.objects.filter(userid=str(request.user)).update(display_picture=request.FILES['display_picture'])
#     x = CustomUser.objects.get(userid=str(request.user))
#     print("Nice entry into if condition")
#     print(type(request.FILES['display_picture'])) 
#     return redirect('settings')

def change_profile_photo(request):
    x = CustomUser.objects.get(userid=str(request.user))
    x.display_picture = request.FILES['display_picture']
    x.save()
    return redirect('settings') 


def change_password(request):
    present_user = str(request.user)
    u = CustomUser.objects.get(userid=present_user)
    if request.method=="POST":
        op=request.POST['op']
        np=request.POST['np']
        cp=request.POST['cp']
        user = auth.authenticate(username=str(request.user),password=op)
        if user is not None:
            if np==cp:
                user.set_password(np)
                user.save()
                return redirect('login')
            else:
                return render(request,'settings.html',{'error':'The new password and confirm new password are not the same. Please check.','present_user':present_user,'u':u})
        else:
             return render(request,'settings.html',{'error':'old password is wrong , please change the password settings again','present_user':present_user,'u':u})

def change_account_type(request):
    n=CustomUser.objects.get(userid=request.user)
    if n.acctype=="Public":
        n.acctype="Private"
        n.save()
    else:
       
        l1=n.foll_req.split()
        for fr in l1:
            n1 = CustomUser.objects.get(userid=fr)
            n1.foll += " "+str(request.user)
            n1.save()
            #n = CustomUser.objects.get(userid=request.user)
            n.followers += " "+fr
            #n.save()
            #n = CustomUser.objects.get(userid=request.user)
            n.foll_req=n.foll_req.replace(" "+fr,"")
            #n.save()
        n.acctype="Public"
        n.save()
    return redirect('settings')