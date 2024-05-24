import hashlib
from flask import jsonify, request
import numpy


# 接口通用返回格式
def json_return(message='', info=[], code=200):
    return jsonify({
        'code': int(code),
        'message': message,
        'info': info,
    })


# 获取请求参数
def get_request_param(fields=[]):
    res = {}
    # get参数
    info = request.args
    if info != None:
        for key in info:
            res[key] = info[key]
    # post参数 json
    info = request.get_json(force=True, silent=True)
    if info != None:
        for key in info:
            res[key] = info[key]
    # post参数x-www-form-urlencoded/form-data
    info = request.form
    if info != None:
        for key in info:
            res[key] = info[key]
    # 筛选需要的字段
    if len(fields) > 0:
        temp = {}
        for field in fields:
            if field in res:
                temp[field] = res[field]
        res = temp

    return res


# numpy数字类型json序列化时，会因为不类型不一致报错，这里统一转为字符串即可
def json_format_numpy(data):
    if isinstance(data, list):
        for k, v in enumerate(data):
            data[k] = json_format_numpy(v)
    elif isinstance(data, dict):
        for k in data:
            data[k] = json_format_numpy(data[k])
    elif isinstance(data, numpy.int32) \
            or isinstance(data, numpy.int64) \
            or isinstance(data, numpy.float32) \
            or isinstance(data, numpy.float64):
        data = str(data)
    return data

# 获取文件md5
def md5_file(file_path):
    md5_obj = hashlib.md5()
    with open(file_path, 'rb') as file_obj:
        md5_obj.update(file_obj.read())
    file_md5_id = md5_obj.hexdigest()
    return file_md5_id
