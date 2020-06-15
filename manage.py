import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis 对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护，只做服务器验证功能，
CSRFProtect(app)
# 设置session保存指定位置
Session(app)
manager=Manager(app,db)
manager.add_command('db', MigrateCommand)
@app.route('/')
def index():
    # 添加一个键值对
    session['name1'] = 'eric'
    return 'index'

if __name__ == '__main__':
    app.run()

