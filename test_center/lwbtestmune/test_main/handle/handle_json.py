# coding=utf-8
import json


def create_json(path):
    open(path, 'w')

def read_json(path):
    '''获取json对象'''
    with open(path, encoding='UTF-8') as f:
        data = json.loads(f.read())
    return data


def get_json_value(path, key):
    """获取json的值"""
    data = read_json(path)
    return data.get(key)


def write_json_value(file_path, data):
    data_value = json.dumps(data)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(data_value)


if __name__ == '__main__':
    print(write_json_value('app'))
