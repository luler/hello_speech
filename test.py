import tool.valid_tool

request = {
    "name": "sss"
}

rules = {
    "name|名称": "required",
    "password|密码": "required",
}

try:
    tool.valid_tool.valid_tool.checkData(request, rules)
except Exception as e:
    print(e)
