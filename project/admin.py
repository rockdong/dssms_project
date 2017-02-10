from django.contrib import admin

# Register your models here.
from project.models import Pro, Actor, ProFlowBlank, PlanFlow, Actual, Action

admin.site.register(Pro)
admin.site.register(Actor)
admin.site.register(ProFlowBlank)
admin.site.register(PlanFlow)
admin.site.register(Actual)
admin.site.register(Action)