import yaml
from jsonpath import jsonpath


class Utils:
    @classmethod
    def base_jsonpath(cls, obj, json_expr):
        '''
        封装 jsonpath
        :param obj: 要断言的响应内容
        :param json_expr: jsonpath 表达式
        :return: 提取内容的列表
        '''
        return jsonpath(obj, json_expr)

    @classmethod
    def get_yaml_data(cls, file_path):
        '''
        读取yaml文件
        :param file_path: 文件路径
        :return: 字典格式的 yaml文件
        '''
        with open(file_path, encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data
