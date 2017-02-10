# coding:utf-8

from django.shortcuts import render, render_to_response
import logging
from company.models import *
from company.forms import *

# Create your views here.

logger = logging.getLogger('views')

# 公司成员登陆界面
def do_login(request):
	try:
		company_login = CompanyLoginForm()
		if request.method == 'POST' :
			company_login = CompanyLoginForm(request.POST)
			if company_login.is_valid():
				# 登陆
				companyname = company_login.cleaned_data["companyname"]
				username = company_login.cleaned_data["username"]
				password = company_login.cleaned_data["password"]
				staff = Staff.objects.get(organization__company_name=companyname, login_name=username, password=password)
				logger.debug(staff.staff_name)
				if staff is not None :
					return render(request, 'cindex.html', {'staff':staff})
				else:
					return render(request, 'clogin.html', {'error':'没有该用户', 'company_login':company_login})
			else:
				logger.error("数据验证失败 : " + company_login.errors)
		return render(request, 'clogin.html', {'company_login': company_login, 'error':company_login.errors})
	except Exception as e:
		logger.error(e)
		return render(request, 'clogin.html', {'company_login':company_login, 'error':''})

#用户注册
def do_regist(request):
	try:
		return render(request, 'regist.html')
	except Exception as e:
		logger.error(e)
		return render(request, 'page_404.html')

#忘记密码
def do_forget(request):
	try:
		return render(request, 'forget.html')
	except Exception as e:
		logger.error(e)
		return render(request, 'page_404.html')

#跳转到 layout_app.html
def layout_app(request):
	try:
		return render(request, 'layout_app.html')
	except Exception as e:
		logger.error(e)
		return render(request, 'page_404.html')

#跳转到 layout_fullwidth.html
def layout_fullwidth(request):
	try:
		return render(request, 'layout_fullwidth.html')
	except Exception as e:
		logger.error(e)
		return render(request, 'page_404.html')

#跳转到 form_element.html
def form_element(request):
	try:
		return render(request, 'form_element.html')
	except Exception as e:
		logger.error(e)
		return render(request, 'page_404.html')