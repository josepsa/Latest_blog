from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.views import generic

app_name='user_accounts_app'

urlpatterns = [
    path('sign_up/',views.SignUp.as_view(),name='signup'),
    path('sign_in/',auth_views.LoginView.as_view(template_name='user_accounts_app/sign_in.html'),name='signin'),
    path('sign_out/',auth_views.LogoutView.as_view(),name='signout'),
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='user_accounts_app/change_password.html'
                                                                 ,success_url=reverse_lazy('user_accounts_app:signin')),
         name='change_password'),
]