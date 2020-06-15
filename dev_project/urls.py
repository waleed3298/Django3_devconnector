from django.contrib import admin
from django.urls import path
from devconnector import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth stuff
    path('signup',views.signupuser,name='signupuser'),
    path('login',views.loginuser,name='loginuser'),
    path('logout',views.logoutuser,name='logoutuser'),
    # All profile stuff
    path('',views.home , name='home'),
    path('dashboard',views.dashboard,name='Dashboard'),
    path('createprofile',views.CreateProfile,name='createprofile'),
    path('<int:profile_pk>/editprofile', views.EditProfile , name = 'editprofile'),
    path('addexperience',views.AddExperience,name='addexperience'),
    path('addeducation',views.AddEducation,name='addeducation'),
    #  All deleting  stuff
    path('<int:profile_pk>', views.deleteprofile,name = 'deleteprofile'),
    path('deleteexperience/<int:work_pk>', views.deleteexperience,name = 'deleteexperience'),
    path('deleteeducation/<int:school_pk>', views.deleteeducation,name = 'deleteeducation'),
    # All other developer stuff
    path('developers', views.Developers,name='developers'),
    path('developerinfo/<slug:the_slug>',views.Developerinfo,name='developerinfo'),
    path('posts',views.viewposts,name='posts'),
    path('comment/<int:post_pk>',views.comment,name='comment'),
    path('deletecomment/<int:post_pk>',views.DeleteComment,name='deletecomment'),
    path('deletepost/<int:post_pk>',views.DeletePost,name='deletepost'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
