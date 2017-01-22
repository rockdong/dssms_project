# coding:utf-8

from django.shortcuts import render
import logging
from company.models import *

# Create your views here.

logger = logging.getLogger('views')

# 公司成员登陆界面
def index(request):
	try:
		if request.method is "POST" :
			company_name = request.GET('company_name', None)
			org = Organization.objects.filter(company_name=company_name)
			if org :
				login_name = request.GET('user_name', None)
				password = request.GET('password', None)
				act = Staff.objects.filter(login_name=login_name, password=password)
				if act :
					render(request, 'index.html', locals())
	except Exception as e:
		logger.error(e)
	finally:
		render(request, 'login.html', locals())