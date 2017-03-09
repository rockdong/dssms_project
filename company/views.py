# coding:utf-8


from django.shortcuts import render, render_to_response, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import logging

from company.models import *
from company.forms import *

# Create your views here.

logger = logging.getLogger('views')


class LoginView(View):
    def get(self, request):
        login_form = CompanyLoginForm()
        return render(request, "login.html", {'login_form': login_form})

    def post(self, request):
        login_form = CompanyLoginForm(request.POST)
        if login_form.is_valid():
            companyname = request.POST.get("companyname", "")
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            user = authenticate(organization__company_name=companyname, username=username, password=password)
            if user is not None:
                request.session['companyname'] = companyname
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'regist.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            '''
				获取页面表格数据
			'''
            company_name = request.POST.get('company_name', "")
            company_license = request.POST.get('company_license', "")
            corporation = request.POST.get('corporation', "")
            sex = request.POST.get('sex', "")
            corporation_contact = request.POST.get('corporation_contact', "")
            user_name = request.POST.get('user_name', "")
            password = request.POST.get('password', "")
            '''
				创建 organization
				    company_name = models.CharField(null=False, max_length=50, primary_key=True, verbose_name='企业名称')
					company_license = models.ImageField(upload_to='license/%s/', \
										blank=False, null=False, verbose_name='营业执照')
					corporation = models.CharField(max_length=20, null=False, blank=False, verbose_name='法人代表')
					corporation_contact = models.CharField(max_length=20, null=False, blank=False, verbose_name='联系方式')
			'''
            organization = Organization()
            organization.company_name = company_name
            organization.corporation = corporation
            organization.corporation_contact = corporation_contact
            organization.save()
            '''
                创建 duty
                    organization = models.ForeignKey(Organization, verbose_name='公司')
                    duty_name = models.CharField(max_length=20,verbose_name='职位名称')
            '''
            duty = Duty()
            duty.organization = organization
            duty.duty_name = "法人"
            duty.save()
            '''
				创建 department
				    organization = models.ForeignKey(Organization, verbose_name='公司')
					department_name = models.CharField(max_length=50, null=False, blank=False, primary_key=True, verbose_name='部门名称')
			'''
            department = Department()
            department.organization = organization
            department.department_name = "法人"
            department.duty = duty
            department.save()
            '''
				创建 skills
				    organization = models.ForeignKey(Organization, verbose_name='公司')
    				skill_name = models.CharField(max_length=20, primary_key=True, verbose_name='技术')
			'''
            skill = Skill()
            skill.organization = organization
            skill.skill_name = "管理"
            skill.save()

            staff = Staff()
            staff.organization = organization
            staff.department = department
            staff.staff_name = corporation
            staff.sex = sex
            staff.username = user_name
            staff.password = make_password(password)
            staff.save()
            return render(request, 'login.html', {})
        else:
            register_form = RegisterForm()
            return render(request, 'regist.html', {'register_form': register_form})


class StaffView(View):
    def get(self, request):
        all_staff = Staff.objects.all()[:5]
        pages = Staff.objects.count() / 20

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_staff, 5, request=request)

        staffs = p.page(page)

        return render(request, 'all_staffs.html', {'staffs': staffs, 'pages': pages})


class AddStaffView(View):
    def get(self, request):
        companyname = request.session['companyname']
        departments = Department.objects.filter(organization__company_name__contains=companyname)
        return render(request, 'add_staffs.html', {'departments': departments})


class AddDepartmentView(View):
    def get(self, request):
        return render(request, 'add_department.html')


    def post(self, request):
        print '````````````'
        companyname = request.session['companyname']
        department_name = request.POST.get('departmentname', '')

        department = Department.objects.filter(organization__company_name__contains=companyname, department_name__contains=department_name)

        if department is None:
            company = Organization.objects.get(company_name__contains=companyname)
            department = Department()
            department.organization = company
            department.save()
            return render(request, 'add_department.html', {'msg':'部门添加完成'})
        else:
            return render(request, 'add_department.html', {'error':'部门已存在, 请重新添加'})




        # organization = models.ForeignKey(Organization, verbose_name='公司')
        # department = models.ForeignKey(Department, verbose_name='部门')
        # staff_name = models.CharField(max_length=20, null=False, blank=False, verbose_name='姓名')
        #
        # sex = models.CharField(choices=sex_char, max_length=1, null=False, blank=False, verbose_name='性别')
        # # login_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='登陆账号')
        # # password = models.CharField(max_length=50, null=False, blank=False, verbose_name='登陆密码')
        # skills = models.ManyToManyField(Skill, verbose_name='技术/能力')
        # date_join = models.DateField(auto_now_add=True, verbose_name='入职时间')
        # date_out = models.DateField(null=True, verbose_name='离职时间')

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


        # def login(request):
        # 	try:
        # 		print request.path
        # 		if request.method == 'POST':
        # 			companyname = request.POST.get('companyname', None)
        # 			username = request.POST.get('username', None)
        # 			password = request.POST.get('password', None)
        # 			staff = Staff.objects.get(organization__company_name=companyname, login_name=username, password=password)
        # 			if staff:
        # 				# return render_to_response(request, 'cindex.html')
        # 				# return index(request, 'cindex')
        # 				return HttpResponseRedirect('/index/cindex.html')
        # 		else:
        # 			return render(request, 'clogin.html')
        # 	except Exception as e:
        # 		logger.error(e)

        # 页面跳转
        # def index(request, value):
        # 	try:
        # 		page = value + ".html"
        # 		return render(request, page)
        # 	except Exception as e:
        # 		logger.error(e)
        # 		return  render(request, 'page_404.html')



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
        # def do_login(request):
        # 	if request.method == "POST":
        # 		companyname = request.POST.get("companyname", "")
        # 		username = request.POST.get("username", "")
        # 		password = request.POST.get("password", "")
        # 		user = authenticate(organization__company_name=companyname, username=username, password=password)
        # 		if user is not None:
        # 			login(request, user)
        # 			return render(request, 'index.html')
        # 	elif request.method == "GET":
        # 		return render(request, "login.html")
        # try:
        # 	company_login = CompanyLoginForm()
        # 	if request.method == 'POST' :
        # 		company_login = CompanyLoginForm(request.POST)
        # 		if company_login.is_valid():
        # 			# 登陆
        # 			companyname = company_login.cleaned_data["companyname"]
        # 			username = company_login.cleaned_data["username"]
        # 			password = company_login.cleaned_data["password"]
        # 			staff = Staff.objects.get(organization__company_name=companyname, login_name=username, password=password)
        # 			logger.debug(staff.staff_name)
        # 			if staff is not None :
        # 				return render(request, 'index.html', {'staff':staff})
        # 			else:
        # 				return render(request, 'login.html', {'error':'没有该用户', 'company_login':company_login})
        # 		else:
        # 			logger.error("数据验证失败 : " + company_login.errors)
        # 	return render(request, 'login.html', {'company_login': company_login, 'error':company_login.errors})
        # except Exception as e:
        # 	logger.error(e)
        # 	return render(request, 'login.html', {'company_login':company_login, 'error':''})
        #
        # #用户注册
        # def do_regist(request):
        # 	try:
        # if request.method == "POST":
        # 	print request.POST.get('company_name', None)
        # 	print request.POST.get('company_license', None)
        # 	print request.POST.get('corporation', None)
        # 	print request.POST.get('sex', None)
        # 	print request.POST.get('corporation_contact', None)
        # 	print request.POST.get('user_name', None)
        # 	print request.POST.get('password', None)
        # 	return render(request, 'regist.html')
        # except Exception as e:
        # 	logger.error(e)
        # 	return render(request, 'page_404.html')


# 忘记密码
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
# 页面跳转
def index(request, value):
    try:
        page = value + ".html"
        print page
        return render(request, page)
    except Exception as e:
        logger.error(e)
        return render(request, 'login.html')

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
