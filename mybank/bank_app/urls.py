from django.contrib import admin
from django.urls import path

from .import views
urlpatterns = [
    path('',views.landingpage,name='landingpage'),
    path('homepage/<cust_id>',views.homepage,name='homepage'),
    path('mylogin/',views.mylogin,name='mylogin'),
    path('mysignup/',views.mysignup,name = 'mysignup'),
    path('landingpage/',views.landingpage,name='landingpage'),
    path('logout/',views.logoutpage,name='logout'),
    path('error404/',views.error_404,name='error404'),
]