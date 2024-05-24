import re

import validator


class valid_tool():
    @staticmethod
    def checkData(params, rules):
        for rule_field in rules:
            temp_rule_field = rule_field
            rule_field = rule_field.split('|')
            rule_field_title = rule_field[0]
            # 存在字段注解就使用
            if len(rule_field) > 1:
                rule_field_title = rule_field[1]
            rule_field = rule_field[0]
            # 一个个验证，不通过就报错
            one_rule = {rule_field: rules[temp_rule_field]}
            results = validator.validate(params, one_rule, return_info=True)
            if not results[0]:  # 验证不通过
                # 错误字段信息，示例：(False, {'name': 'John Doe', 'mail': 'john_doe@gmail.com'}, {'age': {'Min': 'Expected Maximum: 34, Got: 32'}})
                for rule in results[2][rule_field]:
                    msg = {
                        'Accepted': valid_tool.Accepted,
                        'Binary': valid_tool.Binary,
                        'Integer': valid_tool.Integer,
                        'List': valid_tool.List,
                        'Regex': valid_tool.Regex,
                        'String': valid_tool.String,
                        'Alpha': valid_tool.Alpha,
                        'Date': valid_tool.Date,
                        'IP': valid_tool.IP,
                        'Mail': valid_tool.Mail,
                        'Required': valid_tool.Required,
                        'UUIDv1': valid_tool.UUIDv1,
                        'Base32': valid_tool.Base32,
                        'Decimal': valid_tool.Decimal,
                        'IPv4': valid_tool.IPv4,
                        'Max': valid_tool.Max,
                        'RequiredIf': valid_tool.RequiredIf,
                        'UUIDv3': valid_tool.UUIDv3,
                        'Base64': valid_tool.Base64,
                        'Dict': valid_tool.Dict,
                        'IPv6': valid_tool.IPv6,
                        'Min': valid_tool.Min,
                        'Same': valid_tool.Same,
                        'UUIDv4': valid_tool.UUIDv4,
                        'Between': valid_tool.Between,
                        'Hex': valid_tool.Hex,
                        'JSON': valid_tool.JSON,
                        'Octal': valid_tool.Octal,
                        'Size': valid_tool.Size,
                    }.get(rule, valid_tool.defaultRule)(rule_field_title, rules[temp_rule_field])
                    raise Exception(msg)

    @staticmethod
    def defaultRule(rule_field_title, rule):
        return rule_field_title + ' 输入有误'

    @staticmethod
    def Accepted(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的字符串'

    @staticmethod
    def Binary(rule_field_title, rule):
        return rule_field_title + ' 必须为二进制数'

    @staticmethod
    def Integer(rule_field_title, rule):
        return rule_field_title + ' 必须为整型数字'

    @staticmethod
    def List(rule_field_title, rule):
        return rule_field_title + ' 类型有误'

    @staticmethod
    def Regex(rule_field_title, rule):
        return rule_field_title + ' 输入验证失败'

    @staticmethod
    def String(rule_field_title, rule):
        return rule_field_title + ' 必须为字符串'

    @staticmethod
    def Alpha(rule_field_title, rule):
        return rule_field_title + ' 必须为英文字母'

    @staticmethod
    def Date(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的日期'

    @staticmethod
    def IP(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的ip'

    @staticmethod
    def Mail(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的邮箱'

    @staticmethod
    def Required(rule_field_title, rule):
        return rule_field_title + ' 不能为空'

    @staticmethod
    def UUIDv1(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的uuidv1格式'

    @staticmethod
    def Base32(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的base32格式'

    @staticmethod
    def Decimal(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的十进制数'

    @staticmethod
    def IPv4(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的ipv4'

    @staticmethod
    def Max(rule_field_title, rule):
        regex = re.search("max:(\d+)", rule, re.IGNORECASE)
        return rule_field_title + ' 不能大于 ' + regex.group(1)

    @staticmethod
    def RequiredIf(rule_field_title, rule):
        return rule_field_title + ' 不能为空'

    @staticmethod
    def UUIDv3(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的uuidv3格式'

    @staticmethod
    def Base64(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的base64格式'

    @staticmethod
    def Dict(rule_field_title, rule):
        return rule_field_title + ' 类型有误'

    @staticmethod
    def IPv6(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的ipv6'

    @staticmethod
    def Min(rule_field_title, rule):
        regex = re.search("min:(\d+)", rule, re.IGNORECASE)
        return rule_field_title + ' 不能小于 ' + regex.group(1)

    @staticmethod
    def Same(rule_field_title, rule):
        return rule_field_title + ' 输入有误'

    @staticmethod
    def UUIDv4(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的uuidv4格式'

    @staticmethod
    def Between(rule_field_title, rule):
        regex = re.search("between:(\d+),(\d+)", rule, re.IGNORECASE)
        return rule_field_title + ' 必须在 ' + regex.group(1) + ' 到 ' + regex.group(2) + ' 之间'

    @staticmethod
    def Hex(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的十六进制数'

    @staticmethod
    def JSON(rule_field_title, rule):
        return rule_field_title + ' 必须输入有效的json格式'

    @staticmethod
    def Octal(rule_field_title, rule):
        return rule_field_title + ' 必须为有效的八进制数'

    @staticmethod
    def Size(rule_field_title, rule):
        regex = re.search("size:(\d+)", rule, re.IGNORECASE)
        return rule_field_title + ' 大小尺寸必须为 ' + regex.group(1)
