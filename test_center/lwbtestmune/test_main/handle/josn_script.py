import json
from deepdiff import DeepDiff


class touch_result:
    '''判断返回报文与预期结果的报文格式是否一致'''

    def touch_json(self, dict1, dict2):  # , dict1, dict2
        # dict1 = {"aa": "ss", "qq": "1122", "cc": "111"}
        # dict2 = {"aa":"ss","qq":"11","cc":"112"}
        # dict3 = ("aa","ss","qq","11","cc","112")
        # print(DeepDiff(dict1,dict2))
        dict3 = json.loads(dict1)
        dict4 = json.loads(dict2)
        if isinstance(dict3, dict) and isinstance(dict4, dict):
            cmp_dict = DeepDiff(dict3, dict4, ignore_order=True).to_dict()
            if 'dictionary_item_added' in cmp_dict.keys():
                return False
            elif 'dictionary_item_removed' in cmp_dict.keys():
                return False
            elif 'type_changes' in cmp_dict.keys():
                return False
            else:
                return True
        else:
            return False


jsonJudgment = touch_result()
if __name__ == '__main__':
    ss = touch_result()
    ss.touch_json()
