from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='user_accounts_app'

urlpatterns = [
    path('sign_up/',views.SignUp.as_view(),name='signup'),
    path('sign_in/',auth_views.LoginView.as_view(template_name='user_accounts_app/sign_in.html'),name='signin'),
    path('sign_out/',auth_views.LogoutView.as_view(),name='signout'),
]