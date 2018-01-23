#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# froms.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 1/18/2018, 4:57:48 PM
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})
