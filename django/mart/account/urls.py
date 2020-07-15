from django.urls import path,include
from account.views import *
from django.contrib import admin
from account.views import SignUpView,UserUpdateView,UserDetailView,password_reset_complete
# from account.views import SignUpView

urlpatterns = [
    path('',include("django.contrib.auth.urls")),
    
    path("Sign Up",SignUpView.as_view(),name='Sign Up'),

    path("<int:pk>",UserDetailView.as_view(),name='Details'),

    path('<int:pk>/Update',UserUpdateView.as_view(),name='Update'),

    path('password_reset_complete',password_reset_complete,name='password_reset_complete'),
]
