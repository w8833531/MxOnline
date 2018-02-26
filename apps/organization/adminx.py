#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# adminx.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 1/16/2018, 4:44:07 PM
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ('name', 'desc', 'add_time')
    search_fields = ('name', 'desc')
    list_filter = ('name', 'desc', 'add_time')
    model_icon = 'fa fa-university'


class CourseOrgAdmin(object):
    list_display = ('name', 'desc', 'students', 'course_nums', 'click_nums', 'fav_nums',
                    'images', 'address', 'city', 'category', 'add_time')
    search_fields = ('name', 'desc', 'click_nums', 'fav_nums',
                     'images', 'address', 'city')
    list_filter = ('name', 'desc', 'click_nums', 'fav_nums',
                   'images', 'address', 'city', 'add_time')


class TeacherAdmin(object):
    list_display = ('org', 'name', 'work_years', 'work_company',
                    'work_position', 'work_charater', 'click_nums',
                    'fav_nums', 'add_time')
    search_fields = ('org', 'name', 'work_years', 'work_company',
                     'work_position', 'work_charater',
                     'click_nums', 'fav_nums')
    list_filter = ('org__name', 'name', 'work_years', 'work_company',
                   'work_position', 'work_charater', 'click_nums',
                   'fav_nums', 'add_time')


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
