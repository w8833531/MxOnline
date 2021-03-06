from django.db import models
from datetime import datetime

# Create your models here.


class CityDict(models.Model):
    """
    城市信息
    """
    name = models.CharField(
        max_length=20,
        verbose_name="城市名"
    )
    desc = models.CharField(
        max_length=200,
        verbose_name="城市描述"
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    """
    机构信息
    """
    name = models.CharField(
        max_length=50,
        verbose_name="机构名称",
    )
    desc = models.TextField(
        default='',
        verbose_name="机构描述",
    )
    tag = models.CharField(
        default='全国知名',
        max_length=10,
        verbose_name="机构标签"
    )
    category = models.CharField(
        max_length=20,
        choices=(("pxjg", "培训机构"), ("gx", "高校"), ("gr", "个人")),
        verbose_name="机构类别",
        default="pxjg",
    )
    students = models.IntegerField(
        default=0,
        verbose_name="学习人数"
    )
    course_nums = models.IntegerField(
        default=0,
        verbose_name="课程数"
    )
    click_nums = models.IntegerField(
        default=0,
        verbose_name="点击数"
    )
    fav_nums = models.IntegerField(
        default=0,
        verbose_name="收藏数"
    )
    images = models.ImageField(
        upload_to="org/%Y/%m",
        verbose_name="logo",
        max_length=100,
        null=True,
        blank=True)
    address = models.CharField(
        max_length=150,
        verbose_name="机构地址",
    )
    city = models.ForeignKey(
        CityDict,
        verbose_name="所在城市"
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间"
    )

    def __str__(self):
        return self.name

    def get_teacher_nums(self):
        # 获取机构的教师数量
        return self.teacher_set.all().count()

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    """
    教师信息
    """
    org = models.ForeignKey(
        CourseOrg,
        verbose_name="所属机构"
    )
    name = models.CharField(
        max_length=50,
        verbose_name="教师名",
    )
    work_years = models.IntegerField(
        default=0,
        verbose_name="工作年限"
    )
    work_company = models.CharField(
        max_length=50,
        verbose_name="就职公司",
    )
    work_position = models.CharField(
        max_length=50,
        verbose_name="公司职位",
    )
    work_charater = models.CharField(
        max_length=50,
        verbose_name="教学风格",
    )
    image = models.ImageField(
        upload_to="teacher/%Y/%m",
        verbose_name="头像",
        max_length=100,
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        default=0,
        verbose_name="年龄"
    )
    click_nums = models.IntegerField(
        default=0,
        verbose_name="点击数"
    )
    fav_nums = models.IntegerField(
        default=0,
        verbose_name="收藏数"
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name="添加时间"
    )

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_nums(self):
        # 获取讲师的课程数量
        return self.course_set.all().count()
