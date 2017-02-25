from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response, HttpResponse
import logging, json
from company.models import *
#from company.forms import *
from company.serializers import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

logger = logging.getLogger('views')

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def staffs(request, departname):
	try:
		if request.method == 'GET':
			if departname == "all":
				staffs = Staff.objects.all()
				serializer = StaffSerializer(staffs, many=True)
				return JSONResponse(serializer.data)
			else:
				staffs = Staff.objects.get(department__department_name=departname)
				serializer = StaffSerializer(staffs, many=True)
				return JSONResponse(serializer.data)
	except Exception as e:
		logger.error(e)