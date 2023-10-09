# coding=utf-8
import json
import os
from bcpinterface.handles.handle_ini import handle_ini
from bcpinterface.handles.handle_logging import log


def read_header_json():
    '''获取json对象'''
    headers = handle_ini.get_ini_value('header_path')
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/config/' + headers)
    with open(file_path, encoding='UTF-8') as f:
        data = json.loads(f.read())
    return data


def get_header_value(key):
    '''获取header的值'''
    data = read_header_json()
    return data.get(key)[0]


def get_token(res):
    """获取登录接口的token值"""
    res = json.loads(res)
    token = res['data']['accessToken']
    return token


def get_new_header(res):
    """将token赋值给公共header的Authorization"""
    header = get_header_value('headers_public')
    header['Authorization'] = get_token(res)
    return header


def get_new_headers(res):
    """替换旧headers的公共header"""
    data = read_header_json()
    data['headers_public'][0] = get_new_header(res)
    return data


def write_header_value(res):
    """保存替换后的headers"""
    data_value = json.dumps(get_new_headers(res))
    headers = handle_ini.get_ini_value('header_path')
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/config/' + headers)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data_value)
        log.info('登录接口写入access_token成功')


if __name__ == '__main__':
    print(read_header_json().get('headers_public')[0])
    print(get_header_value('headers_public'))
