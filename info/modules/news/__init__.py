# 创建蓝图
from flask import Blueprint
news_blu=Blueprint('new',__name__,url_prefix="/news")
from . import views