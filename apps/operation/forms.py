#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# forms.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 2/1/2018, 11:21:54 AM
import re
from django import forms
from operation.models import UserConsult


class UserConsultForm(forms.ModelForm):
    class Meta:
        model = UserConsult
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
