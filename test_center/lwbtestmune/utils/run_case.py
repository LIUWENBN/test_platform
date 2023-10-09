# conding=utf-8
import json
from lwbtestmune.test_main.basePage.base_method import base_pages
from lwbtestmune.model.project_model import CaseModel
from django.shortcuts import redirect, reverse
from lwbtestmune.test_main.handle.handle_relations import handleRelations
from lwbtestmune.test_main.handle.handle_logging import log


def RunCase(case_id, is_run, method, base_url, url, verify_value, page, data=None, header=None, relation=None, relation_key=None):

    case = CaseModel.objects.get(pk=case_id)

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
            rep = base_pages.request_main(method, url, data, header)
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
        return redirect(reverse(page))
    else:
        case.is_pass = '用例已禁用'
        case.save()
        return redirect(reverse(page))