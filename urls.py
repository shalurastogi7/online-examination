from django.urls import path
from Examapp.views import *
urlpatterns=[
    path('index',index,name="Homepage"),
    path('signup',signup,name="signup"),
    path('login',loginup,name="login"),
    path('Tsignup',signUp,name="signup"),
    path('Tlogin',loginUP,name="loginup"),
    path('admin',admin,name="admin"),
    path('contact',contact,name="contact"),
    path('tdashboard',tdashboard,name="tdashboard"),
    path('mcourse',mcourse,name="mcourse"),
    path('mquestion',mquestion,name="mquestion"),
    path('addexam',addexam,name="addexam"),
    path('viewexam',viewexam,name="viewexam"),
    path('viewquestion',viewquestion,name="viewquestion"),
    path('addquestion',addquestion,name="addquestion"),


    
]