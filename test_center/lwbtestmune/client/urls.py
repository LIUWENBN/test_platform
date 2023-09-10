# coding=utf-8

from django.urls import path
from .views.index import Index
from .views.project_list import ProjectList, ProjectDelete, UpdateProjectStatus, ProjectEdit, ProjectView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('projectList', ProjectList.as_view(), name='project_list'),
    path('projectDelete/<int:project_id>', ProjectDelete.as_view(), name='project_delete'),
    path('projectUpdateStatus/<int:project_id>', UpdateProjectStatus.as_view(), name='project_update_status'),
    path('projectEdit/<int:project_id>', ProjectEdit.as_view(), name='project_edit'),
    path('projectView/<int:project_id>', ProjectView.as_view(), name='project_view'),
]