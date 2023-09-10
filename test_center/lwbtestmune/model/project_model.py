# coding=utf-8
from django.db import models
from enum import Enum


class ProjectType(Enum):
    inside = 'inside'
    outside = 'outside'
ProjectType.inside.label = '自研产品'
ProjectType.outside.label = '外部承接'

class ProjectModel(models.Model):
    project_name = models.CharField(max_length=20, null=False)
    project_code = models.CharField(max_length=20, null=False, unique=True)
    project_type = models.CharField(max_length=50, null=False, default=ProjectType.inside.value)
    project_status = models.BooleanField(default=True, db_index=True)
    project_info = models.TextField(max_length=100, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __int__(self):
        return  self.project_name

    @classmethod
    def project_add(cls, project_name, project_code, project_type, project_info=None):
        return cls.objects.create(
            project_name=project_name,
            project_code=project_code,
            project_info=project_info,
            project_type=project_type,
            project_status = True
        )

    @classmethod
    def get_project(cls, project_code):
        try:
            project = cls.objects.get(
                project_code=project_code
            )
            return project
        except:
            print('没有匹配的项目')
            return None

    def update_status(self):
        self.project_status = not self.project_status
        self.save()
        return True