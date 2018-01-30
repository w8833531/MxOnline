from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from .models import UserProfile, EmailVerifyRecode
from .froms import *
from utils.email_send import send_register_email

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **Kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecode.objects.filter(
            code=active_code, send_type="register")
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email, username=email)
                user.is_active = True
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecode.objects.filter(
            code=reset_code, send_type="forget")
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "forget_fail.html")


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不匹配"})
            else:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd1)
                user.save()
                return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})


class RegisterView(View):
    def get(self, request):
        reigster_form = RegisterForm()
        return render(request, "register.html",
                      {'register_form': reigster_form}
                      )

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            if UserProfile.objects.filter(Q(username=user_name) | Q(email=user_name)):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()
            send_register_email(user_name, "register")
            return render(request, "login.html")
        else:
            return render(request,
                          "register.html",
                          {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html",
                                  {"msg": "用户没有激活，请激活后再登录"})
                    # auto send active email again
                    send_register_email(user_name, "register")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误"})
        else:
            return render(request, "login.html", {"login_form": login_form})


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")
            if not UserProfile.objects.filter(Q(username=email) | Q(email=email)):
                return render(request, "forgetpwd.html", {"msg": "用户不存在"})
            send_register_email(email, "forget")
            return render(request, "send_mail_success.html", {"forget_form": forget_form})
        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})
