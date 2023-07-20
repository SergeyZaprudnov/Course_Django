from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from user.form import UserRegisterForm, UserProfileForm
from user.models import User
from user.utils import send_verification_email


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_verification_email(new_user)
        return redirect('user:verify_sent')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self, queryset=None):
        return self.request.user


class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('user:email_confirm')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = uidb64
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user


class VerifyEmailSentView(View):
    def get(self, request):
        return render(request, 'user/verify_sent.html')


class EmailConfirmedView(TemplateView):
    template_name = 'user/email_confirm.html'


class UserPasswordResetView(PasswordResetView):
    email_template_name = 'user/registration/pass_res_email.html'
    template_name = 'user/registration/pass_res_form.html'
    success_url = reverse_lazy('user:pass_res_done')


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'user/registration/pass_res_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'user/registration/pass_res_confirm.html'
    success_url = reverse_lazy("user:pass_res_complete")


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'user/registration/pass_res_complete.html'
