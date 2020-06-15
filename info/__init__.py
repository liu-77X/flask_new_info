import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
from config import Config

app = Flask(__name__)

def create_app():
    pass

app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis 对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护，只做服务器验证功能，
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

# 编写方法进行变换（生产，测试等）