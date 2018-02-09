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
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^teacher/(?P<org_id>\d+)/$',
        OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏URL
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
    # 讲师列表页
    url(r'^teacher/list/$', TeacherListView.as_view(), name="teacher_list"),
    # 讲师详情页
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$',
        TeacherDetailView.as_view(), name="teacher_detail"),
]
