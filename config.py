import logging

import redis


class Config(object):
    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information14"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


    # 日志级别
    LEVEL=logging.DEBUG

# 开发环境
class DevelopConfig(Config):
    pass
# 生产环境
class ProductConfig(Config):
    DEBUG = False
    LEVEL=logging.ERROR

# 测试环境
class TestingConfig(Config):
    TESTING=True

# 通过统一的额字典进行配置类的访问
config_dict={
    "develop":DevelopConfig,
    "product":ProductConfig,
    "testing":TestingConfig
}