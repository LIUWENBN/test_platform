# coding=utf-8

from django.urls import path
from .views.index import Index
from .views.project_list import ProjectList, ProjectDelete, UpdateProjectStatus, ProjectEdit, ProjectView
from .views.business_list import BusinessList, BusinessDelete, BusinessUpdate, BusinessView, RunSingleBusiness
from .views.case_lsit import CaseList, CaseDelete, CaseUpdate, CaseUpdateStatus, CaseView, RunSingleCase
from .views.tabe_pull import TablePull


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('projectList', ProjectList.as_view(), name='project_list'),
    path('projectDelete/<int:project_id>', ProjectDelete.as_view(), name='project_delete'),
    path('projectUpdateStatus/<int:project_id>', UpdateProjectStatus.as_view(), name='project_update_status'),
    path('projectEdit/<int:project_id>', ProjectEdit.as_view(), name='project_edit'),
    path('projectView/<int:project_id>', ProjectView.as_view(), name='project_view'),
    path('businessScene', BusinessList.as_view(), name='business_list'),
    path('runSingleBusiness/<int:business_id>', RunSingleBusiness.as_view(), name='run_single_business'),
    path('businessView/<int:business_id>', BusinessView.as_view(), name='business_view'),
    path('businessDelete/<int:business_id>', BusinessDelete.as_view(), name='business_delete'),
    path('businessUpdate/<int:business_id>', BusinessUpdate.as_view(), name='business_update'),
    path('caseList', CaseList.as_view(), name='case_list'),
    path('caseView/<int:case_id>', CaseView.as_view(), name='case_view'),
    path('caseDelete/<int:case_id>', CaseDelete.as_view(), name='case_delete'),
    path('caseUpdate/<int:case_id>', CaseUpdate.as_view(), name='case_update'),
    path('caseUpdateStatus/<int:case_id>', CaseUpdateStatus.as_view(), name='case_update_status'),
    path('runSingleCase/<int:case_id>', RunSingleCase.as_view(), name='run_single_case'),
    path('tablePull', TablePull.as_view(), name='table_pull'),
]