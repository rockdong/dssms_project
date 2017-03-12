"""dssms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from company.views import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^regist', RegisterView.as_view(), name='regist'),
    url(r'^forget', do_forget, name='forget'),
    url(r'^index/all_staffs$', StaffView.as_view(), name='all_staffs'),
    url(r'^index/add_staffs$', AddStaffView.as_view(), name='add_staffs'),
    url(r'^index/add_departments$', AddDepartmentView.as_view(), name='add_departments'),
    url(r'^index/add_duties$', AddDutyView.as_view(), name='add_duties'),
    url(r'^data/get_duties$', GetDutiesView.as_view(), name='get_duties'),
    url(r'^index/(\w*)$', index, name='index'),
    url(r'^captcha', include('captcha.urls')),
]
