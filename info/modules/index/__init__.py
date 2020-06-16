#创建蓝图
from flask import Blueprint
index_blu=Blueprint('iondex',__name__)
from . import views