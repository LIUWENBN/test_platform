# coding=utf-8
from django.db import models
from enum import Enum


class ProjectType(Enum):
    inside = 'inside'
    outside = 'outside'
ProjectType.inside.label = '自研产品'
ProjectType.outside.label = '外部承接'


class MethodType(Enum):
    po = 'POST'
    GE = 'GET'
    PU = 'PUT'
    DE = 'DELETE'
    HE = 'HEAD'
    TR = 'TRACE'
    OP = 'OPTIONS'
    CO = 'CONNECT'
MethodType.po.label = 'POST'
MethodType.GE.label = 'GET'
MethodType.PU.label = 'PUT'
MethodType.DE.label = 'DELETE'
MethodType.HE.label = 'HEAD'
MethodType.TR.label = 'TRACE'
MethodType.OP.label = 'OPTIONS'
MethodType.CO.label = 'CONNECT'

class ProjectModel(models.Model):
    project_name = models.CharField(max_length=20, null=False)
    project_code = models.CharField(max_length=20, null=False, unique=True)
    project_type = models.CharField(max_length=50, null=False, default=ProjectType.inside.value)
    project_status = models.BooleanField(default=True, db_index=True)
    base_url = models.CharField(max_length=100, default='')
    project_header = models.TextField(max_length=200, default='')
    project_method =  models.CharField(max_length=20, blank=False, null=False, default=MethodType.GE.value)
    login_url = models.CharField(max_length=100, default='')
    project_data = models.TextField(default='')
    token_name = models.CharField(max_length=100, null=False, default='')
    project_info = models.TextField(max_length=100, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __int__(self):
        return  self.project_name

    @classmethod
    def project_add(cls, project_name, project_code, project_type, base_url, project_method, login_url, token_name, project_data=None, project_header=None, project_info=None):
        return cls.objects.create(
            project_name=project_name,
            project_code=project_code,
            project_info=project_info,
            project_type=project_type,
            base_url=base_url,
            project_method=project_method,
            login_url=login_url,
            token_name=token_name,
            project_data=project_data,
            project_header=project_header,
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

    @classmethod
    def get_all_projects(cls, ):
        try:
            all_projects = cls.objects.all()
            return all_projects
        except:
            print('获取项目失败')
            return None

    def update_status(self):
        self.project_status = not self.project_status
        self.save()
        return True

class BusinessModel(models.Model):
    business_name = models.CharField(max_length=20, null=False)
    business_code = models.CharField(max_length=20, null=False, unique=True)
    owner_project = models.ForeignKey(ProjectModel, related_name='business', on_delete=models.SET_NULL, blank=True, null=True)
    case_count = models.CharField(max_length=20, default=0)
    run_count = models.CharField(max_length=20, default=0)
    skip_count = models.CharField(max_length=20, default=0)
    pass_ratio = models.CharField(max_length=20, default=0)
    test_report = models.CharField(max_length=200, default='')
    run_log = models.CharField(max_length=200, default='')
    business_info = models.TextField(max_length=100, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __int__(self):
        return  self.business_name

    @classmethod
    def business_add(cls, business_name, business_code, owner_project, business_info=None):
        return cls.objects.create(
            business_name=business_name,
            business_code=business_code,
            owner_project=owner_project,
            business_info=business_info
        )


class VerifyType(Enum):
    code = 'CODE'
    json = 'JSON'
    codemsg = 'CODEANDMSG'
VerifyType.code.label = 'CODE'
VerifyType.json.label = 'JSON'
VerifyType.codemsg.label = 'CODEMSG'


class CaseModel(models.Model):
    case_name = models.CharField(max_length=20, null=False)
    owner_project = models.ForeignKey(ProjectModel, related_name='case', on_delete=models.SET_NULL, blank=True,
                                      null=True)
    owner_business = models.ForeignKey(BusinessModel, related_name='case', on_delete=models.SET_NULL, blank=True,
                                      null=True)
    relation = models.CharField(max_length=200, default='')
    relation_key = models.CharField(max_length=100, default='')
    case_status = models.BooleanField(default=True, db_index=True)
    header = models.TextField(max_length=200, default='')
    method = models.CharField(max_length=20, blank=False, null=False, default=MethodType.GE.value)
    url = models.CharField(max_length=100, blank=False, null=False)
    data = models.TextField(default='')
    exp_result = models.TextField(default='')
    real_result = models.TextField(default='')
    verify_type = models.CharField(max_length=20, blank=False, null=False, default=VerifyType.code.value)
    is_pass = models.CharField(max_length=20, default='')
    case_info = models.TextField(max_length=100, default='')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_waite =  models.CharField(max_length=6, default='')
    serial_num = models.CharField(max_length=10, unique=True, default='')
    verify_value = models.TextField(default='')


    def __int__(self):
        return  self.case_name

    class Meta:
        unique_together = ('case_name', 'owner_project', 'owner_business')

