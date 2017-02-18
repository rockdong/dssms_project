# coding:utf-8

from rest_framework import serializers
from project.models import *

class ProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = ('org', 'pro_name')


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('pro', 'pro_actors')


class ProFlowBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProFlowBlank
        fields = ('pro', 'pro_flow_name')


class PlanFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFlow
        fields = ('pro_flow_blank', 'pre_st_date', 'pre_ed_date')


class ActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actual
        fields = ('pro_flow_blank', 'act_st_date', 'act_ed_date')

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('pro_flow_blank', 'action_content', 'action_type')


# # 参考 # #
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')