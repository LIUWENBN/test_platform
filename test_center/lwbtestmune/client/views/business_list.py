# coding=utf-8
import time
from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from lwbtestmune.lib.render_response import render_to_response
from lwbtestmune.model.project_model import BusinessModel, ProjectModel, CaseModel
from lwbtestmune.utils.run_case import RunCase
from lwbtestmune.utils.serial import orderretrun


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
        cases = CaseModel.objects.filter(owner_business=business).order_by('serial_num')
        data = {'business': business, 'owner_project':owner_project, 'all_project':all_project, 'cases':cases}

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


class TablePull(View):

    def post(self, request):
        cases = CaseModel.objects.all().order_by('serial_num')
        newindex = request.POST.get('newIndex', '')
        oldIndex = request.POST.get('oldIndex', '')
        print('返回序号--->', newindex, type(newindex), oldIndex, type(oldIndex))

        try:
            orderretrun(cases, int(newindex), int(oldIndex))
            return JsonResponse({'code': 0, 'msg': '排序调整成功~', 'cases': cases})
        except:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '排序调整出错~'})

class RunSingleBusiness(View):

    def get(self, request, business_id):
        business = BusinessModel.objects.get(pk=business_id)
        cases = CaseModel.objects.filter(owner_business=business).order_by('serial_num')
        case_count = len(cases)
        page = 'business_list'
        pass_num = 0
        skip_num = 0
        for case in cases:
            case_id=case.id
            is_run = case.case_status
            relation = case.relation
            relation_key = case.relation_key
            header = case.header
            method = case.method
            url = case.url
            data = case.data
            exp_result = case.exp_result
            verify_type = case.verify_type
            verify_value = case.verify_value
            is_waite = case.is_waite
            single_project = case.owner_project
            base_url = single_project.base_url
            RunCase(case_id, is_run, method, base_url, url, verify_value, page, data, header, relation, relation_key)

            if is_waite:
                time.sleep(is_waite)
            if case.is_pass == '成功':
                pass_num = pass_num + 1
            if case.is_pass == '用例已禁用':
                skip_num = skip_num + 1

        run_count = case_count - skip_num
        pass_ratio = (pass_num/run_count)*100

        business.case_count=case_count
        business.run_count=run_count
        business.skip_count=skip_num
        business.pass_ratio=pass_ratio
        business.save()
        return redirect(reverse('business_list'))
