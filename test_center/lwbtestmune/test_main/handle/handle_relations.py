# coding=utf-8
import json
from jsonpath_rw import parse
from lwbtestmune.test_main.handle.handle_logging import log
from lwbtestmune.model.project_model import CaseModel


class handle_relations:
    def get_relation_keys(self, relation_key=None):
        """获取relation_keys以集合输出"""
        if relation_key is None:
            print('接口特殊relation_key为空')
        else:
            return relation_key.split('>')

    def get_relations(self, relation=None):
        """获取多个关联关系以集合输出"""
        if relation is None:
            print('请填写关联关系')
        else:
            return relation.split('#')

    def get_relation(self, relation):
        """解析关联关系用例编号和路径码以集合输出"""
        relations = self.get_relations(relation)
        case_id_list = []
        relations_list = []
        for i in relations:
            case_nums = i.split('>')[0]
            case_id_list.append(case_nums)
            call_datas = i.split('>')[1]
            relations_list.append(call_datas)
        return case_id_list, relations_list

    def get_relation_result(self, relation):
        """获取多个用例编号对应行码的实际结果以集合输出"""
        case_id_list = self.get_relation(relation)[0]
        real_results = []
        for oi in case_id_list:
            case = CaseModel.objects.get(pk=oi)
            real_result = case.real_result
            real_results.append(real_result)
        return real_results

    def myReplace(self, data, match, repl):
        if isinstance(data, (dict, list)):
            for k, v in (data.items() if isinstance(data, dict) else enumerate(data)):
                if k == match:
                    data[k] = repl
                self.myReplace(v, match, repl)

    def get_relation_datas(self, relation):
        """循环实际结果集合，循环路径码，解析对应实际结果拿到关联字段值以集合输出"""
        relationdatas = []
        i = 0
        for cell_data in self.get_relation_result(relation):
            relationdata = []
            if cell_data is not None:
                relation_cell_data1 = json.loads(cell_data)
            else:
                print(str(i) + '行关联关系书写错误')
                relation_cell_data1 = None
            json_expr = parse(self.get_relation(relation)[1][i])
            modles = json_expr.find(relation_cell_data1)
            for math in modles:
                relationdata.append(math.value)
            relationdatas.append(relationdata)
            i = i + 1
        return relationdatas

    def get_new_data(self, method, relation, data, relation_keys=None):
        """data的relation数据写入与格式转换"""
        if relation is not None:
            relation_keys = self.get_relation_keys(relation_keys)
            log.info("relation_keys：{}".format(relation_keys))
            realtions = self.get_relation_datas(relation)
            log.info("relations：{}".format(realtions))
            for i in range(len(realtions)):
                if isinstance(data, dict) and relation_keys is not None:
                    # if isinstance(data[relation_keys[i]], list):
                    #     data[relation_keys[i]] = realtions[i]
                    # else:
                    #     data[relation_keys[i]] = realtions[i][0]
                    if relation_keys[i] in data.keys():
                        if isinstance(data[relation_keys[i]], list):
                            data[relation_keys[i]] = realtions[i]
                        else:
                            self.myReplace(data, relation_keys[i], realtions[i][0])
                    else:
                        self.myReplace(data, relation_keys[i], realtions[i][0])
                if relation_keys is None and data is not None:
                    if method == 'GET':
                        data = str(data).replace('#' + str(i), str(realtions[i][0]))
                    elif data == '{}':
                        data = data
                    elif method == 'DELETE':
                        data = realtions[i]
                        data = json.dumps(data)
                    else:
                        data = data
            if isinstance(data, dict):
                data = json.dumps(data)
            else:
                data = data
        else:
            if isinstance(data, dict):
                data = json.dumps(data)
            else:
                data = data
        return data

    def str_json(self, data):
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    def datas_return(self, method, relation, data, relation_keys=None):
        if data is not None:
            if method == 'GET':
                data = data
            elif data == '{}':
                data = data
            elif self.str_json(data) is True:
                data = json.loads(data)
            else:
                data = data
            return self.get_new_data(method, relation, data, relation_keys)
        else:
            data = None
            return data

    def url_return(self, url, relation):
        url = url.replace('#', str(self.get_relation_datas(relation)[0][0]))
        return url


handleRelations = handle_relations()
if __name__ == '__main__':
    method = 'POST'
    url = '/api/bcp-system/role'
    data = {"roleName":"id不能特别大会超标","roleCode":"GNJS406849679875200","appMenus":[{"id":1,"appCode":"BSPT10005380152702314112","menus":[{"id":3,"code":"SMNU321370826484768"}]}]}
    prerequisites = 'bcp_interface_024>data#bcp_interface_023>data.[0].appCode#bcp_interface_023>data.[0].menus.[0].code'
    relationkeys = 'roleCode>appCode>code'
    ss = handle_relations()
    # print(ss.str_json(data))
    # print('关联到的数据-->', ss.datas_return(method, prerequisites, data))
    # print(ss.get_relation_datas(prerequisites))
    print('最终data值-->', ss.get_new_data(method, prerequisites, data, relationkeys))
    print('最终data值类型-->', type(ss.get_new_data(method, prerequisites, data, relationkeys)))
    # print('最终data值-->', ss.datas_return(method, prerequisites, data, relationkeys))
    # print('最终data值类型-->', type(ss.datas_return(method, prerequisites, data, relationkeys)))

