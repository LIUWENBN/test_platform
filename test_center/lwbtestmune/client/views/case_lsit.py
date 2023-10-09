# coding=utf-8
import json
from django.views.generic import View
from django.core.paginator import Paginator
from django.shortcuts import redirect, reverse
from django.http import JsonResponse
from lwbtestmune.lib.render_response import render_to_response
from lwbtestmune.model.project_model import BusinessModel, ProjectModel, CaseModel
from lwbtestmune.test_main.basePage.base_method import base_pages
from lwbtestmune.test_main.handle.handle_relations import handleRelations
from lwbtestmune.test_main.handle.handle_logging import log

class CaseList(View):
    TEMPLATE = 'client/case_list.html'

    def get(self, request):

        all_project = ProjectModel.objects.all()
        all_business = BusinessModel.objects.all()

        cases = CaseModel.objects.all().order_by('-pk')
        length = len(cases)
        page = request.GET.get('page', 1)
        p = Paginator(cases, 10)
        total_page = p.num_pages
        if int(page) <= 1:
            page = 1
        current_page = p.get_page(int(page)).object_list
        data = {'cases': current_page, 'total': total_page, 'page_num': int(page), 'all_project':all_project,'all_business':all_business, 'len':length}

        return render_to_response(request, self.TEMPLATE, data=data)

    def post(self, request):
        case_name = request.POST.get('case_name', '')
        serial_num = request.POST.get('serial_num','')
        owner_project = request.POST.get('owner_project', '')
        owner_business = request.POST.get('owner_business', '')
        case_relation = request.POST.get('case_relation', '')
        case_relation_key = request.POST.get('case_relation_key', '')
        case_header = request.POST.get('case_header', '')
        case_method = request.POST.get('case_method', '')
        case_url = request.POST.get('case_url', '')
        case_data = request.POST.get('case_data', '')
        case_exp_result = request.POST.get('case_exp_result', '')
        case_verify_type = request.POST.get('case_verify_type', '')
        case_verify_value = request.POST.get('verify_value','')
        case_waite = request.POST.get('case_waite', '')
        case_info = request.POST.get('case_info', '')
        case_id = request.POST.get('case_id', '')

        if not case_verify_value:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '请输入验证值~'})
        if not serial_num:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '请输入用例序号~'})
        if not case_name:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '用例名称不能为空~'})
        if not case_method:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '用例请求方式不能为空~'})
        if not case_url:
            return JsonResponse({'code': -1, 'log': 'fail', 'msg': '用例请求路径不能为空~'})
        if case_verify_type == 'JSON':
            if not case_exp_result:
                return JsonResponse({'code': -1, 'log': 'fail', 'msg': '验证方式为JSON,用例预期结果不能为空~'})


        project = ProjectModel.objects.get(pk=owner_project)
        business = BusinessModel.objects.get(pk=owner_business)

        if case_id:
            case = CaseModel.objects.get(pk=case_id)
            case.case_name=case_name
            case.owner_project=project
            case.owner_business=business
            case.relation=case_relation
            case.relation_key=case_relation_key
            case.header=case_header
            case.method=case_method
            case.url=case_url
            case.data=case_data
            case.exp_result=case_exp_result
            case.verify_type=case_verify_type
            case.is_waite=case_waite
            case.case_info=case_info
            case.serial_num=serial_num
            case.verify_value=case_verify_value
            case.save()
            return JsonResponse({'code': 0, 'msg': '修改用例成功~'})
        else:
            CaseModel.objects.create(
                case_name=case_name,
                owner_project=project,
                owner_business=business,
                relation=case_relation,
                relation_key=case_relation_key,
                header=case_header,
                method=case_method,
                url=case_url,
                data=case_data,
                exp_result=case_exp_result,
                verify_type=case_verify_type,
                is_waite=case_waite,
                serial_num=serial_num,
                verify_value=case_verify_value,
                case_info=case_info
            )
            return JsonResponse({'code': 0, 'msg': '创建用例成功~'})


class CaseView(View):
    TEMPLATE = 'client/case_view.html'

    def get(self, request, case_id):

        case = CaseModel.objects.get(pk=case_id)
        all_project = ProjectModel.objects.all()
        all_business = BusinessModel.objects.all()
        owner_project = case.owner_project
        owner_business = case.owner_business
        data = {'single_case': case, 'owner_project': owner_project, 'all_project': all_project,
                'owner_business': owner_business, 'all_business': all_business}

        return render_to_response(request, self.TEMPLATE, data=data)


class CaseUpdate(View):
    TEMPLATE = 'client/case_update.html'

    def get(self, request, case_id):

        case = CaseModel.objects.get(pk=case_id)
        all_project = ProjectModel.objects.all()
        all_business = BusinessModel.objects.all()
        owner_project = case.owner_project
        owner_business = case.owner_business
        data = {'single_case': case, 'owner_project':owner_project, 'all_project':all_project, 'owner_business':owner_business, 'all_business':all_business}

        return render_to_response(request, self.TEMPLATE, data=data)


class CaseDelete(View):

    def get(self, request, case_id):

        CaseModel.objects.filter(id=case_id).delete()

        return redirect(reverse('case_list'))


class CaseUpdateStatus(View):

    def get(self, request, case_id):

        case = CaseModel.objects.get(id=case_id)
        case.case_status = not case.case_status
        case.save()

        return redirect(reverse('case_list'))


class RunSingleCase(View):

    def get(self, request, case_id):

        case = CaseModel.objects.get(id=case_id)
        log.info('执行用例:{}'.format(case))
        is_run = case.case_status
        relation = case.relation
        log.info('关联关系:{}'.format(relation))
        relation_key = case.relation_key
        log.info('关联字段:{}'.format(relation_key))
        header = case.header
        method = case.method
        url = case.url
        log.info('取出url:{}'.format(url))
        data = case.data
        log.info('取出参数:{}'.format(data))
        exp_result = case.exp_result
        verify_type = case.verify_type
        is_waite = case.is_waite
        single_project = case.owner_project
        base_url = single_project.base_url
        serial_num = case.serial_num
        verify_value = case.verify_value

        if not all([method, url]):
            case.is_pass = '缺少必要字段~'
            case.save()
            return redirect(reverse('case_list'))

        if relation:
            data = handleRelations.datas_return(method, relation, data, relation_key)
            if not data or data == '{}':
                url = handleRelations.url_return(url, relation)
        log.info('入参参数:{}'.format(data))
        url = base_url + url
        log.info('入参url:{}'.format(url))
        header = json.loads(header)
        if is_run:
            try:
                rep = base_pages.request_main(method,url, data, header)
                log.info('响应报文:{}'.format(rep))
                rep = json.loads(rep)
                if rep['code'] == verify_value:
                    case.is_pass = '成功'
                    case.real_result = json.dumps(rep)
                    case.save()
                else:
                    case.is_pass = '失败'
                    case.real_result = json.dumps(rep)
                    case.save()
            except:
                case.is_pass = '运行错误'
                case.save()
            return redirect(reverse('case_list'))
        else:
            case.is_pass = '用例已禁用'
            case.save()
            return redirect(reverse('case_list'))




