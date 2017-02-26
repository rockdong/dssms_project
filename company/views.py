# coding:utf-8


from django.shortcuts import render, render_to_response, HttpResponse
# from company.forms import *
import logging

from company.models import *
from company.forms import *

# Create your views here.

logger = logging.getLogger('views')

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
# @csrf_exempt
# def staffs(request, departname):
# 	try:
# 		if request.method == 'GET':
# 			if departname == "all":
# 				staffs = Staff.objects.all()
# 				serializer = StaffSerializer(staffs, many=True)
# 				return JSONResponse(serializer.data)
# 			else:
# 				staffs = Staff.objects.get(department__department_name=departname)
# 				serializer = StaffSerializer(staffs, many=True)
# 				return JSONResponse(serializer.data)
# 	except Exception as e:
# 		logger.error(e)
#
#


def login(request):
	try:
		print request.path
		if request.method == 'POST':
			companyname = request.POST.get('companyname', None)
			username = request.POST.get('username', None)
			password = request.POST.get('password', None)
			staff = Staff.objects.get(organization__company_name=companyname, login_name=username, password=password)
			if staff:
				# return render_to_response(request, 'cindex.html')
				# return index(request, 'cindex')
				return HttpResponseRedirect('/index/cindex.html')
		else:
			return render(request, 'clogin.html')
	except Exception as e:
		logger.error(e)

#页面跳转
def index(request, value):
	try:
		page = value + ".html"
		return render(request, page)
	except Exception as e:
		logger.error(e)
		return  render(request, 'page_404.html')



# # 参考 # #
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

# # 改动之前的代码 # #
# 公司成员登陆界面
def login(request):
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
					return render(request, 'index.html', {'staff':staff})
				else:
					return render(request, 'login.html', {'error':'没有该用户', 'company_login':company_login})
			else:
				logger.error("数据验证失败 : " + company_login.errors)
		return render(request, 'login.html', {'company_login': company_login, 'error':company_login.errors})
	except Exception as e:
		logger.error(e)
		return render(request, 'login.html', {'company_login':company_login, 'error':''})
#
#用户注册
def do_regist(request):
	try:
		if request.method == "POST":
			print request.POST.get('company_name', None)
			print request.POST.get('company_license', None)
			print request.POST.get('corporation', None)
			print request.POST.get('sex', None)
			print request.POST.get('corporation_contact', None)
			print request.POST.get('user_name', None)
			print request.POST.get('password', None)
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
#
# #跳转到 layout_app.html
# def layout_app(request):
# 	try:
# 		return render(request, 'layout_app.html')
# 	except Exception as e:
# 		logger.error(e)
# 		return render(request, 'page_404.html')
#
# #跳转到 layout_fullwidth.html
# def layout_fullwidth(request):
# 	try:
# 		return render(request, 'layout_fullwidth.html')
# 	except Exception as e:
# 		logger.error(e)
# 		return render(request, 'page_404.html')
#
# #跳转到 form_element.html
# def form_element(request):
# 	try:
# 		return render(request, 'form_element.html')
# 	except Exception as e:
# 		logger.error(e)
# 		return render(request, 'page_404.html')
#
#页面跳转
def index(request, value):
	try:
		page = value + ".html"
		print page
		return render(request, page)
	except Exception as e:
		logger.error(e)
		return  render(request, 'login.html')

# # 获取所有员工数据
# def getAllStaffs(request):
# 	try:
# 		if request.method == "GET":
# 			staffs = Staff.objects.all()
# 			rs = {}
# 			rs['result'] = 'hello'
# 			rs['message'] = 'world'
# 			return HttpResponse({'staffs':staffs})
# 	except Exception as e:
# 		logger.error(e)
# 		return render(request, 'page_404.html')