#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# froms.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 1/18/2018, 4:57:48 PM
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
