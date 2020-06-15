# 只负责基本的启动
# app的创建在info文件下的init文件中
from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import app, db
# flask_script
manager = Manager(app)
# 数据库迁移
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session['name'] = 'eric'
    return "index"
if __name__ == '__main__':
    manager.run()
