import api.common_api

# 接口路由，全部写在这里
from tool import common


def add_new_routes(app):
    # 全局异常捕获处理
    @app.errorhandler(Exception)
    def errorhandler(error):
        error = str(error)
        code = 400
        if error == '授权凭证无效':
            code = 401
        return common.json_return(error, [], code)

    @app.before_first_request
    def before_first_request_instance():
        pass

    @app.before_request
    def before_request_instance():
        pass

    # 自定义路由
    app.add_url_rule('/api/test', view_func=api.common_api.test, methods=['POST', 'GET'])
    app.add_url_rule('/api/tts', view_func=api.common_api.tts, methods=['POST', 'GET'])
    app.add_url_rule('/api/asr', view_func=api.common_api.asr, methods=['POST'])
    app.add_url_rule('/api/punctuation', view_func=api.common_api.punctuation, methods=['POST', 'GET'])
