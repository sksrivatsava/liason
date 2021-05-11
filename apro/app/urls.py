from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.page0_base,name='base'),
    path('page1_home/',views.page1_home,name='home'),
    path('page2_friends/',views.page2_friends,name='friends'),
    path('page3_register/',views.page3_register,name='register'),
    path('page4_login/',views.page4_login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('page5_following',views.page5_following,name='following'),
    path('page6_follow_requests',views.page6_follow_requests,name='follow_requests'),
    path('page7_create_post',views.page7_create_post,name='create_post'),
    path('page8_profile/<fr>/',views.page8_profile,name='profile'),
    path('f/<fr>/',views.follow,name='f'),
    path('uf/<fr>/',views.unfollow,name='uf'),
    path('frq/<fr>/',views.follow_request,name='frq'),
    path('ac/<fr>/',views.accept_follow_request,name='ac'),
    path('rc/<fr>/',views.reject_follow_request,name='rc'),
    path('upvote/',views.upvote,name='upvote'),
    path('downvote/',views.downvote,name='upvote'),
    path('settings/',views.settings,name="settings"),
    path('change_password/',views.change_password,name="change_password"),
    path('change_account_type/',views.change_account_type,name="change_account_type"),
    path('change_username/',views.change_username,name="change_username"),
    path('change_profile_photo/',views.change_profile_photo,name="change_profile_photo")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)