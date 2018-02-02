#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# url.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 2/1/2018, 3:23:03 PM

from django.conf.urls import url, include

from .views import *


urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserConsultView.as_view(), name="add_ask"),
]
