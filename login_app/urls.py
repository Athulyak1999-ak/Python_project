from django.urls import path
from . import views

urlpatterns = [

    path('', views.loginPage, name='login'),
    path('register/', views.userRegistration, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('user_view/', views.user_view, name='user_view'),
    path('logout/', views.logout_view, name='logout')

]
