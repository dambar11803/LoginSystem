from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name='dashboard.html'
    login_url='/'    #redirect to login page

class HomePage(LoginRequiredMixin, TemplateView):
    template_name='homepage.html'
    login_url='/'     #redirect to login page

