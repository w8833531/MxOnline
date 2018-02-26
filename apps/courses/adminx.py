#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# adminx.py
# @Author : 吴鹰 (wuying@corp.the9.com)
# @Link   :
# @Date   : 1/16/2018, 2:14:34 PM

import xadmin

from .models import Course, BannerCourse, Lesson, Video, CourseResource


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学后台管理"
    site_footer = "慕学在线"
    menu_style = "accordion"


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail',
                    'degree', 'click_nums', 'learn_times', 'student_nums', 'fav_nums', 'get_zj_nums']
    search_fields = ('name', 'desc', 'detail',
                     'degree', 'learn_times', 'student_nums', 'fav_nums')
    list_filter = ('name', 'desc', 'detail',
                   'degree', 'learn_times', 'student_nums', 'fav_nums')
    list_editable = ['name', 'desc', 'detail',
                     'degree', 'learn_times', 'student_nums', 'fav_nums']
    model_icon = 'fa fa fa-envelope-open'
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    relfield_style = 'fk-ajax'
    inlines = [LessonInline, CourseResourceInline]
    refresh_times = [15, 30, 45, 60]

    # 重载父类的queryset方法，过虑出is_banner=True的数据
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    # 重载父类的 save_models 方法，自动更新机构课程数
    def save_models(self):
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(
                course_org=course_org).count()
            course_org.save


# 只显示广告课程is_banner=True
class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'detail',
                    'degree', 'click_nums', 'learn_times', 'student_nums', 'fav_nums', 'get_zj_nums']
    search_fields = ('name', 'desc', 'detail',
                     'degree', 'learn_times', 'student_nums', 'fav_nums')
    list_filter = ('name', 'desc', 'detail',
                   'degree', 'learn_times', 'student_nums', 'fav_nums')
    model_icon = 'fa fa fa-envelope-open'
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    relfield_style = 'fk-ajax'
    inlines = [LessonInline, CourseResourceInline]

    # 重载父类的queryset方法，过虑出is_banner=True的数据
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class VideoInline(object):
    model = Video
    extra = 0


class LessonAdmin(object):
    list_display = ('course', 'name', 'add_time')
    search_fields = ('course', 'name')
    list_filter = ('course__name', 'name', 'add_time')
    inlines = [VideoInline]


class VideoAdmin(object):
    list_display = ('lesson', 'name', 'add_time')
    search_fields = ('lesson', 'name')
    list_filter = ('lesson__name', 'name', 'add_time')


class CourseResourceAdmin(object):
    list_display = ('course', 'name', 'download', 'add_time')
    search_fields = ('course', 'name', 'download')
    list_filter = ('course__name', 'name', 'download', 'add_time')


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
