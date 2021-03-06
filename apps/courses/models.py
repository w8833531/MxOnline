from django.db import models
from datetime import datetime
from organization.models import CourseOrg, Teacher
from DjangoUeditor.models import UEditorField

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(
        CourseOrg, verbose_name="课程机构", null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher, verbose_name="讲师", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = UEditorField(verbose_name="课程详情", width=600, height=300,
                          imagePath="courses/ueditor/", filePath="courses/ueditor/", default="")
    is_banner = models.BooleanField(default=False, verbose_name="是否为广告位")
    degree = models.CharField(
        choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")),
        max_length=2, verbose_name="难度")
    learn_times = models.IntegerField(
        default=0,
        verbose_name="学习时长(小时)")
    student_nums = models.IntegerField(
        default=0,
        verbose_name="学习人数")
    fav_nums = models.IntegerField(
        default=0,
        verbose_name="收藏人数")
    images = models.ImageField(
        upload_to="courses/%Y/%m",
        verbose_name="封面图",
        max_length=100,
        null=True,
        blank=True)
    click_nums = models.IntegerField(
        default=0,
        verbose_name="点击数")
    category = models.CharField(
        default="后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(
        default="", max_length=100, verbose_name="课程标签")
    youneed_know = models.CharField(
        default="", max_length=300, verbose_name="课程须知")
    teacher_tell = models.CharField(
        default="", max_length=300, verbose_name="教师告诉你")
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 返回课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数"

    def get_learn_users(self):
        # 返回学习用户数
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 返回课程章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name


# BannerCourse 类用于xamdin 中显示一个广告课程的菜单
class BannerCourse(Course):
    class Meta:
        verbose_name = "广告课程"
        verbose_name_plural = verbose_name
        # 继承Course类，设置proxy = True 时，不再生成新表
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(
        max_length=100,
        verbose_name="章节名")
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        # 返回课程章节视频
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(
        max_length=100,
        verbose_name="视频名")
    url = models.CharField(
        default="",
        max_length=200,
        verbose_name="访问链接")
    learn_times = models.IntegerField(
        default=0,
        verbose_name="学习时长(分钟)")
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(
        max_length=100,
        verbose_name="名称"
    )
    download = models.FileField(
        upload_to='resource/%Y/%m',
        verbose_name="资源文件",
        max_length=100
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间"
    )

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
