from flask import render_template, current_app, session

from . import index_blu
from ... import constants
from ...models import User, News, Category


@index_blu.route('/')
def index():
    # 首页显示
    # 获取当前登录用户的id信息
    user_id=session.get("user_id")
    # 通过id查询用户信息
    user=None
    news_list=None
    if user_id:
        try:
            user=User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)
    try:
        news_list=News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)
    click_news_list=[]
    for news in news_list if news_list else []:
        click_news_list.append(news.to_basic_dict())
    # 获取新闻分类的数据
    categories_dicts=[]
    categories=Category.query.all()
    for category in categories:
        categories_dicts.append(category.to_dict())

    data={
        "user_info": user.to_dict() if user else None,
        "click_news_list":click_news_list,
        "categories":categories_dicts
          }

    return render_template('news/index.html',data=data)


@index_blu.route('/favicon.ico')
def get_web_logo():
    return current_app.send_static_file('news/favicon.ico')