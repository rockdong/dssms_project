from django.contrib import admin

# Register your models here.
from project.models import Pro, Actor, ProFlowBlank, PlanFlow, Actual, Pic, Process, Subitem

admin.site.register(Pro)
admin.site.register(Actor)
admin.site.register(ProFlowBlank)
admin.site.register(PlanFlow)
admin.site.register(Actual)
admin.site.register(Pic)
admin.site.register(Process)
admin.site.register(Subitem)