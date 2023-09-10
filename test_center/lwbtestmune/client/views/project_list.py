# coding=utf-8

from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from lwbtestmune.lib.render_response import render_to_response
from lwbtestmune.model.project_model import ProjectModel

class ProjectList(View):
    TEMPLATE = 'client/project_list.html'

    def get(self, request):

        projects = ProjectModel.objects.all().order_by('-pk')
        length = len(projects)

        page = request.GET.get('page', 1)
        p = Paginator(projects, 10)
        total_page = p.num_pages
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(int(page)).object_list
        data={'projects': current_page, 'total':total_page, 'page_num':int(page), 'len':length}

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):

        project_name = request.POST.get('project_name', '')
        project_code = request.POST.get('project_code', '')
        project_type = request.POST.get('project_type', '')
        project_info = request.POST.get('project_info', '')
        project_id = request.POST.get('project_id', '')

        if not project_name:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '项目名称不能为空~'})

        if project_id:

            project = ProjectModel.objects.filter(pk=project_id)[0]
            project.project_name = project_name
            project.project_code = project_code
            project.project_type = project_type
            project.project_info = project_info
            project.save()

            return JsonResponse({'code': 0, 'msg': '修改项目成功~'})

        else:

            if not project_code:
                return JsonResponse({'code': -1, 'msg': '项目编码不能为空~'})
            exists = ProjectModel.objects.filter(project_code=project_code).exists()
            if exists:
                return JsonResponse({'code': -1, 'log': 'fail', 'msg': '项目编码重复，请重新填写~'})
            ProjectModel.project_add(
                project_name=project_name,
                project_code=project_code,
                project_type=project_type,
                project_info=project_info
            )
            return JsonResponse({'code': 0,'msg': '创建项目成功~'})


class ProjectView(View):
    TEMPLATE = 'client/project_view.html'

    def get(self, request, project_id):

        project = ProjectModel.objects.filter(pk=project_id)[0]
        data = {'project': project}

        return render_to_response(request, self.TEMPLATE, data=data)


class ProjectEdit(View):
    TEMPLATE = 'client/project_edit.html'

    def get(self, request, project_id):

        project = ProjectModel.objects.filter(pk=project_id)[0]
        data = {'project': project}

        return render_to_response(request, self.TEMPLATE, data=data)


class ProjectDelete(View):

    def get(self, request, project_id):

        ProjectModel.objects.filter(id=project_id).delete()

        return redirect(reverse('project_list'))


class UpdateProjectStatus(View):

    def get(self, request, project_id):

        project = ProjectModel.objects.get(pk=project_id)
        project.project_status = not project.project_status
        project.save()
        return redirect(reverse('project_list'))




