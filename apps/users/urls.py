#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# url.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 2/12/2018, 2:32:24 PM
from django.conf.urls import url, include

from .views import *


urlpatterns = [
    # 用户信息
    url(r'^info/$', UserinfoView.as_view(), name="user_info"),
    # 用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
    # 我的收藏-机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    # 我的收藏-讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 我的收藏-课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),
]
