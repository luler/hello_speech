# flask变量
# ENV = 'production'
import orator_database

ENV = 'development'

HOST = '0.0.0.0'
PORT = 5000
THREADED = False
PROCESSES = 1

# 自定义变量
# 数据库配置
DATABASES = orator_database.DATABASES
# CAS配置
CAS_CONFIG = {
    'host': 'https://cas.luler.top',
    'appid': '',
    'appsecret': '',
}
