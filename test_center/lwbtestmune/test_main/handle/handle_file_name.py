import os
import shutil


def change_filename(dir_path):
    file_path = os.path.join(dir_path, 'html')
    os.chdir(file_path)
    old_filename = 'index.html'
    new_filename = 'bcp接口测试报告.html'
    os.rename(old_filename, new_filename)


# 第一种：删除一个文件夹，无论里面是否有文件或文件夹
# (不支持文件，文件夹不存在会报错)
def del_files0(dir_path):
    shutil.rmtree(dir_path)


# 第二种 递归删除dir_path目标文件夹下所有文件，以及各级子文件夹下文件，保留各级空文件夹
# (支持文件，文件夹不存在不报错)
def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path)  # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            # if file_name != 'wibot.log':
            tf = os.path.join(dir_path, file_name)
            del_files(tf)
    print('ok')


# 第三种： 删除dir_path目标文件夹下所有内容，保留dir_path文件夹
# (不支持文件，文件夹不存在会报错)
def del_files2(dir_path):
    print(dir_path)
    # os.walk会得到dir_path下各个后代文件夹和其中的文件的三元组列表，顺序自内而外排列， 如 log下有111文件夹，111下有222文件夹：[('D:\\log\\111\\222', [],
    # ['22.py']), ('D:\\log\\111', ['222'], ['11.py']), ('D:\\log', ['111'], ['00.py'])]
    for root, dirs, files in os.walk(dir_path, topdown=False):
        # print(root)  # 各级文件夹绝对路径
        # print(dirs)  # root下一级文件夹名称列表，如 ['文件夹1','文件夹2']
        # print(files)  # root下文件名列表，如 ['文件1','文件2']
        # 第一步：删除文件
        for name in files:
            os.remove(os.path.join(root, name))  # 删除文件
        # 第二步：删除空文件夹
        for name in dirs:
            os.rmdir(os.path.join(root, name))  # 删除一个空目录


if __name__ == '__main__':
    dir_path = 'F:/PycharmPyProject/bcpinterface/report'
    del_files(dir_path)
