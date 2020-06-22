from flask import render_template, current_app, session, request, jsonify

from . import index_blu
from ... import constants
from ...models import User, News, Category
from ...utils.response_code import RET


@index_blu.route('/newlist')
def get_news_list():
    # 获取参数
    args_dict=request.args
    page=args_dict.get('page',1)#第几页
    per_page=args_dict.get('per_page',constants.HOME_PAGE_MAX_NEWS)#一夜多少数据
    category_id=args_dict.get('cid',1)
    # 校验参数
    try:
        page=int(page)
        per_page=int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR,errsg="参数错误")
    # 查询数据并分页
    filters = []
    if category_id!="1":
        filters.append(News.category_id==category_id)
    try:
        pagnite=News.query.filter(*filters).order_by(News.create_time.desc()).pagnite(page, per_page, False)
        # 获取查询的数据
        items=pagnite.items
        # 获取总页数
        total_page=pagnite.pages
        current_page=pagnite.page
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errsg="数据获取失败")
    new_li=[]
    for news in items:
        new_li.append(news.to_basic_dict())
    return jsonify(errno=RET.OK, errsg="OK",total_page=total_page,current_page=current_page,newsList=new_li,cid=category_id)

    # 返回数据

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