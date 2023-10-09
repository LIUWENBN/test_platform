# import json
# from bcpinterface.handles.handle_json import get_json_value
#
#
# class code_msg:
#
#     def code_msg_test(self, url, code):
#         file_path = handle_ini.get_ini_value('code_msg_path', 'bcp_info')
#         ss = get_json_value(url, file_path)
#         if ss is not None:
#             for i in ss:
#                 msg = i.get(str(code))
#                 if msg:
#                     return msg
#         else:
#             return None
#
#
# CodeMsg = code_msg()
# if __name__ == '__main__':
#     run = code_msg()
#     print(run.code_msg_test('/api/bcp-console/conf/component/#', '0'))
