from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm, UserProfileEditForm
from django.views import View
import random
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password']
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accounts:verify_code')
        return render(request, self.template_name, {'form': form})


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/verify.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['full_name'], user_session['password'])

                code_instance.delete()
                messages.success(request, 'you registered.', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'this code is wrong', 'danger')
                return redirect('accounts:verify_code')
        return redirect('home:home')


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'info')
                return redirect('home:home')
            messages.error(request, 'phone or password is wrong', 'warning')
        return render(request, self.template_name, {'form': form})


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')


class UserPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'  # this is template for password reset form
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class UserProfileView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return render(request, 'accounts/profile.html', {'user': user})


class UserProfileEditView(View):
    def get(self, request):
        form = UserProfileEditForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})

    def post(self, request):
        form = UserProfileEditForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile successfully updated', 'success')
            return redirect('accounts:user_profile', request.user.id)
        return render(request, 'accounts/edit_profile.html', {'form': form})
