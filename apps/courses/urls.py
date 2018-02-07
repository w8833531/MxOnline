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
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$',
        CourseDetailView.as_view(), name="course_detail"),

    url(r'^info/(?P<course_id>\d+)/$',
        CourseInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$',
        CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),
]
