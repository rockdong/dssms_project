# coding:utf-8

from rest_framework import serializers
from company.models import *

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('company_name', 'company_license', 'corporation',
                    'corporation_contact', 'date_regedit')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('organization', 'role_name', 'level')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('organization', 'department_name', 'role')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('organization', 'skill_name')


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'organization', 'department', 'staff_name', 'sex',
                'login_name', 'password', 'skills', 'date_join', 'date_out')


# # 参考 # #
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')