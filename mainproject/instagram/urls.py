from django.urls import path
from instagram.views import LoginView, UserRegistrationView, UserView, ProfileView, CreatePageView, LogoutView, CreateContentView, DeleteContentView, UpdateContentView
urlpatterns=[
    path('login/',
     LoginView.as_view(),
     name='login'),
     path('userregistration/',
         UserRegistrationView.as_view(),
         name='userregistration'),
     path('user/',
         UserView.as_view(),
         name='user'),
     path('profile/',
         ProfileView.as_view(),
         name='profile'),
     path('createpage/', 
          CreatePageView.as_view(),
          name='createpage'),
     path('logout/',
          LogoutView.as_view(),
          name='logout'),
     path('createcontent/',
          CreateContentView.as_view(),
          name='createcontent'),
     path('updatecontent/<int:id>/',
          UpdateContentView.as_view(),
          name='updatecontent'),
     path('deletecontent/',
          DeleteContentView.as_view(),
          name='deletecontent'),

]