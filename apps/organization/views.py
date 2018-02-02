# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import CourseOrg, CityDict
from operation.forms import *


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
            return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')
