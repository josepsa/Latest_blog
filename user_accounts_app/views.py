from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from . import forms

from django.contrib.auth import views as auth_views




class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('user_accounts_app:signin')
    template_name = 'user_accounts_app/sign_up.html'
    



