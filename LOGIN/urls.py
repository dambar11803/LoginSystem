"""
URL configuration for LOGIN project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authenticate.views import DashBoard, HomePage
from django.contrib.auth import views as auth_views 
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('dashboard/', DashBoard.as_view(), name='dashboard'),
     path('homepage/', HomePage.as_view(), name='homepage'),
    #path('index/', IndexPage.as_view(), name='index'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html'), name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name= 'registration/password_change.html'), name='passwordchange'),
     path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name= 'registration/password_change_done.html'), name='password_change_done'),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name='registration/PasswordReset/password_reset_form.html'), name="passwordreset"), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/PasswordReset/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/PasswordReset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/PasswordReset/password_reset_complete.html'), name='password_reset_complete'),

   
]
