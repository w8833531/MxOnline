#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# adminx.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 1/15/2018, 10:20:27 AM
import xadmin

from .models import EmailVerifyRecode, Banner


class EmailVerifyRecodeAdmin(object):
    list_display = ('email', 'code', 'send_type', 'send_time')
    search_fields = ['email', 'code', 'send_type']
    list_filter = ('email', 'code', 'send_type', 'send_time')


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'index')
    search_fields = ('title', 'image', 'url', 'index')
    list_filter = ('title', 'image', 'url', 'index', 'add_time')


xadmin.site.register(EmailVerifyRecode, EmailVerifyRecodeAdmin)
xadmin.site.register(Banner, BannerAdmin)
