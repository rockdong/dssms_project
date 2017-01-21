from django.contrib import admin

# Register your models here.
from company.models import Organization, Role, Department, Skill, Staff

admin.site.register(Organization)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Skill)
admin.site.register(Staff)