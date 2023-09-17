# coding=utf-8

from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from lwbtestmune.lib.render_response import render_to_response
from lwbtestmune.model.project_model import BusinessModel, ProjectModel

class BusinessList(View):
    TEMPLATE = 'client/business_list.html'

    def get(self, request):

        all_project = ProjectModel.objects.all()
        business = BusinessModel.objects.all().order_by('-pk')
        length = len(business)
        page = request.GET.get('page', 1)
        p = Paginator(business, 10)
        total_page = p.num_pages
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(int(page)).object_list

        data = {'business': current_page, 'total': total_page, 'page_num': int(page), 'all_project':all_project, 'len':length}

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        business_name = request.POST.get('business_name', '')
        business_code = request.POST.get('business_code', '')
        owner_project = request.POST.get('owner_project', '')
        business_info = request.POST.get('business_info', '')
        business_id = request.POST.get('business_id', '')

        if not business_name:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '业务流程名称不能为空~'})

        if business_id:
            project = ProjectModel.objects.get(pk=owner_project)
            business = BusinessModel.objects.filter(pk=business_id)[0]
            business.business_name=business_name
            business.owner_project=project
            business.business_info=business_info
            business.save()
            return JsonResponse({'code': 0, 'msg': '修改业务流程成功~'})
        else:

            if not business_code:
                return JsonResponse({'code': -1, 'log': 'fail', 'msg': '业务流程编码不能为空~'})
            exists = BusinessModel.objects.filter(business_code=business_code).exists()
            if exists:
                return JsonResponse({'code': -1, 'log': 'fail', 'msg': '业务流程编码重复，请重新填写~'})
            if not owner_project:
                return JsonResponse({'code': -1, 'log': 'fail', 'msg': '业务流程所属项目不能为空~'})

            project = ProjectModel.objects.get(pk=owner_project)
            BusinessModel.business_add(
                business_name=business_name,
                business_code=business_code,
                owner_project=project,
                business_info=business_info
            )
            return JsonResponse({'code': 0, 'msg': '创建业务流程成功~'})


class BusinessView(View):
    TEMPLATE = 'client/business_view.html'

    def get(self, request, business_id):

        all_project = ProjectModel.objects.all()
        business = BusinessModel.objects.filter(pk=business_id)[0]
        owner_project = business.owner_project
        data = {'business': business, 'owner_project':owner_project, 'all_project':all_project}

        return render_to_response(request, self.TEMPLATE, data=data)

class BusinessUpdate(View):
    TEMPLATE = 'client/business_update.html'

    def get(self, request, business_id):

        all_project = ProjectModel.objects.all()
        business = BusinessModel.objects.filter(pk=business_id)[0]
        owner_project = business.owner_project
        data = {'business': business, 'owner_project':owner_project, 'all_project':all_project}

        return render_to_response(request, self.TEMPLATE, data=data)


class BusinessDelete(View):

    def get(self, request, business_id):

        BusinessModel.objects.filter(id=business_id).delete()

        return redirect(reverse('business_list'))