# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import CourseOrg, CityDict
from operation.forms import *
from operation.models import *
from courses.models import Course


class OrgView(View):
    '''
    课程机构列表功能
    '''

    def get(self, request):
        # 获取所有课程机构和机构数
        all_orgs = CourseOrg.objects.all()
        # 获取热门机构的倒序排列
        hot_orgs = all_orgs.order_by("-students")[:5]
        # 获取所有城市
        all_cities = CityDict.objects.all()
        # 取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 筛选类别
        category = request.GET.get('ct', "")
        if category:
            all_orgs = all_orgs.filter(category=category)
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")
        # 统计机构家数
        org_nums = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)

        orgs = p.page(page)
        # city_id = int(city_id)
        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_cities": all_cities,
            "org_nums": org_nums,
            "city_id": city_id,
            "category": category,
            "hot_orgs": hot_orgs,
            "sort": sort,
        })


class AddUserConsultView(View):
    def post(self, request):
        user_consult_form = UserConsultForm(request.POST)
        if user_consult_form.is_valid():
            user_consult = user_consult_form.save(commit=True)
            return HttpResponse(
                '{"status":"success"}',
                content_type='application/json'
            )
        else:
            return HttpResponse(
                '{"status":"fail", "msg":"添加出错"}',
                content_type='application/json'
            )


class OrgHomeView(View):
    """
    机构详情首页
    """

    def get(self, request, org_id):
        current_page = "home"
        # 通过request的org_id,获取机构对象
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 通过机构对象，获取机构关联课程（course_set.all)
        all_courses = course_org.course_set.all()[:3]
        # 通过机构对象，获取机构关联教师（techer_set.all)
        all_teachers = course_org.teacher_set.all()[:2]
        # 返回机构详情页
        return render(
            request,
            'org-detail-homepage.html',
            {
                'all_courses': all_courses,
                'all_teachers': all_teachers,
                'course_org': course_org,
                'current_page': current_page,
                'has_fav': has_fav,
            },
        )


class OrgCourseView(View):
    """
    机构课程列表页
    """

    def get(self, request, org_id):
        current_page = "course"
        # 通过request的org_id,获取机构对象
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 通过机构对象，获取机构关联课程（course_set.all)
        all_courses = course_org.course_set.all()
        # 返回机构课程详情页
        return render(
            request,
            'org-detail-course.html',
            {
                'all_courses': all_courses,
                'course_org': course_org,
                'current_page': current_page,
                'has_fav': has_fav,
            },
        )


class OrgDescView(View):
    """
    机构介绍页
    """

    def get(self, request, org_id):
        current_page = "desc"
        # 通过request的org_id,获取机构对象
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 返回机构课程详情页
        return render(
            request,
            'org-detail-desc.html',
            {
                'course_org': course_org,
                'current_page': current_page,
                'has_fav': has_fav,
            },
        )


class OrgTeacherView(View):
    """
    机构教师列表页
    """

    def get(self, request, org_id):
        current_page = "teacher"
        # 通过request的org_id,获取机构对象
        course_org = CourseOrg.objects.get(id=int(org_id))
        # 用户是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # 通过机构对象，获取机构关联教师（course_set.all)
        all_teachers = course_org.teacher_set.all()
        # 返回机构课程详情页
        return render(
            request,
            'org-detail-teachers.html',
            {
                'all_teachers': all_teachers,
                'course_org': course_org,
                'current_page': current_page,
                'has_fav': has_fav,
            },
        )


class AddFavView(View):
    """
    用户收藏
    """

    def post(self, request):
        fav_id = request.POST.get('fav_id', '0')
        fav_type = request.POST.get('fav_type', '0')

        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}',
                                content_type='application/json')

        exist_records = UserFavorite.objects.filter(
            user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            # 减少相应课程、机构、教师的收藏数
            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.fav_nums -= 1
                if course.fav_nums < 0:
                    course.fav_nums = 0
                course.save()
            elif int(fav_type) == 2:
                course_org = CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_nums -= 1
                if course_org.fav_nums < 0:
                    course_org.fav_nums = 0
                course_org.save()
            elif int(fav_type) == 3:
                teacher = Teacher.objects.get(id=int(fav_id))
                teacher.fav_nums -= 1
                if teacher.fav_nums < 0:
                    teacher.fav_nums = 0
                teacher.save()
            # 去掉“已收藏”，返回“收藏”信息
            return HttpResponse('{"status":"success", "msg":"收藏"}',
                                content_type='application/json')
        else:
            # 用户记录不存在，增加用户收藏
            user_fav = UserFavorite()
            user_fav.user = request.user
            user_fav.fav_id = int(fav_id)
            user_fav.fav_type = int(fav_type)
            user_fav.save()
            # 增加相应课程、机构、教师的收藏数
            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.fav_nums += 1
                course.save()
            elif int(fav_type) == 2:
                course_org = CourseOrg.objects.get(id=int(fav_id))
                course_org.fav_nums += 1
                course_org.save()
            elif int(fav_type) == 3:
                teacher = Teacher.objects.get(id=int(fav_id))
                teacher.fav_nums += 1
                teacher.save()
            # 返回已收藏信息
            return HttpResponse('{"status":"success", "msg":"已收藏"}',
                                content_type='application/json')
