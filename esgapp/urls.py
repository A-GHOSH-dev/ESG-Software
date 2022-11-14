from django.contrib import admin
from django.urls import path, include
from esgapp import views

admin.site.site_header ="Developer Ananya Ghosh"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [

    
    path('', views.index, name='index'),
    path('userdashboardpage/<str:ik>', views.userdashboardpage, name='userdashboardpage'),
    path('userprofile/<str:ik>', views.userprofile, name='userprofile'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('login', views.handleLogin, name='handleLogin'),
    path('approverdashboard/<str:pk>', views.approverdashboard, name='approverdashboard'),
    path('approverprofile/<str:pk>', views.approverprofile, name='approverprofile'),
    path('checkpage/<str:ik>/<str:hk>', views.checkpage, name='checkpage'),
    path('approvercreateprofile', views.approvercreateprofile, name='approvercreateprofile'),
    path('usercreateprofile', views.usercreateprofile, name='usercreateprofile'),
    path('userlist', views.userlist, name='userlist'),
    path('approverlist', views.approverlist, name='approverlist'),
    path('searchpage', views.searchpage, name='searchpage'),
    path('approverprofileview/<str:pk>', views.approverprofileview, name='approverprofileview'),
    path('userprofileview/<str:ik>', views.userprofileview, name='userprofileview'),
    path('reportpdf/<str:ik>/<str:hk>', views.reportpdf, name='reportpdf'),
    path('esgreportingform', views.esgreportingform, name='esgreportingform'),
    
    

]