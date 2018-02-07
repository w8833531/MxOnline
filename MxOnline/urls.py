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

import xadmin


from users.views import *
from organization.views import *


# from xadmin.plugins import xversion

# xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
# xversion.register_models()

urlpatterns = [
    # 管理站点xadmin url
    url(r'^xadmin/', xadmin.site.urls),
    # 首页 url
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
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
    # 更改密码
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    # 机构URL
    url(r'^org/', include('organization.urls', namespace="org")),
    # 课程URL
    url(r'^course/', include('courses.urls', namespace="course")),
]
