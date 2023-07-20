from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user.apps import UserConfig
from user.views import ProfileView, VerifyEmailView, RegisterView, VerifyEmailSentView, EmailConfirmedView, \
    UserPasswordResetView, UserPasswordResetConfirmView, UserPasswordResetDoneView, UserPasswordResetCompleteView

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/<str:uidb64>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('verify_email_sent/', VerifyEmailSentView.as_view(), name='verify_sent'),
    path('email_confirmed/', EmailConfirmedView.as_view(), name='email_confirm'),
    path('password/reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/<str:uidb64>/<str:token>/', UserPasswordResetConfirmView.as_view(), name='pass_res_confirm'),
    path('password/reset/done/', UserPasswordResetDoneView.as_view(), name='pass_res_done'),
    path('password/reset/complete/', UserPasswordResetCompleteView.as_view(), name='pass_res_complete')
]