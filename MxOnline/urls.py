"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin


from users.views import *
from organization.views import *
# from MxOnline.settings import STATIC_ROOT


# from xadmin.plugins import xversion

# xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# xversion.register_models()

urlpatterns = [
    # 管理站点xadmin url
    url(r'^xadmin/', xadmin.site.urls),
    # 首页 url
    url('^$', IndexView.as_view(), name="index"),
    # 登录 url
    url('^login/$', LoginView.as_view(), name="login"),
    # 注册 url
    url('^register/$', RegisterView.as_view(), name="register"),
    # 忘记密码 url
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 注册码 url
    url(r'^captcha/', include('captcha.urls')),
    # 激活 url
    url(r'^active/(?P<active_code>.*)/$',
        ActiveUserView.as_view(), name="user_active"),
    # 重置密码 url
    url(r'^reset/(?P<reset_code>.*)/$',
        ResetView.as_view(), name="reset_pwd"),
    # 用户登出
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # 更改密码
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    # 机构URL
    url(r'^org/', include('organization.urls', namespace="org")),
    # 课程URL
    url(r'^course/', include('courses.urls', namespace="course")),
    # 用户URL
    url(r'^users/', include('users.urls', namespace="users")),
    # 增加富文本 DjangoUedit url
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    # 配置静态文件路径
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]

# 全局404页面配置
hander404 = 'users.views.page_not_found'
# 全局500页面配置
hander500 = 'users.views.page_error'
