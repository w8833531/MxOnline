#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# adminx.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 1/16/2018, 2:14:34 PM

import xadmin

from .models import Course, Lesson, Video, CourseResource


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学后台管理"
    site_footer = "慕学在线"
    menu_style = "accordion"


class CourseAdmin(object):
    list_display = ('name', 'desc', 'detail',
                    'degree', 'learn_times', 'student_nums', 'fav_nums')
    search_fields = ('name', 'desc', 'detail',
                     'degree', 'learn_times', 'student_nums', 'fav_nums')
    list_filter = ('name', 'desc', 'detail',
                   'degree', 'learn_times', 'student_nums', 'fav_nums')


class LessonAdmin(object):
    list_display = ('course', 'name', 'add_time')
    search_fields = ('course', 'name')
    list_filter = ('course__name', 'name', 'add_time')


class VideoAdmin(object):
    list_display = ('lesson', 'name', 'add_time')
    search_fields = ('lesson', 'name')
    list_filter = ('lesson__name', 'name', 'add_time')


class CourseResourceAdmin(object):
    list_display = ('course', 'name', 'download', 'add_time')
    search_fields = ('course', 'name', 'download')
    list_filter = ('course__name', 'name', 'download', 'add_time')


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
