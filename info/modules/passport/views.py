from flask import request, jsonify, current_app, make_response
from info.utils.captcha.captcha import captcha
from . import passport_blu
from ... import redis_store, constants
from ...utils.response_code import RET


@passport_blu.route('/image_code')
def get_image_code():
    # 导入验证码工具
    #1、获取参数
    # args过去？之后的参数
    cur_id=request.args.get('cur_id')
    pre_id=request.args.get('pre_id')
    if not cur_id:
        return jsonify(errno=RET.PARAMERR,errmsg='参数不全')
    try:
        name,text,image_data=captcha.generate_captcha()
    #     保存到redis中
        redis_store.set('image_code:%s'%cur_id,text,constants.IMAGE_CODE_REDIS_EXPIRES)
        if pre_id:
            redis_store.delete('image_code:%s'%[pre_id])
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR,errmsg='验证操作失败')
    # 返回验证码图片
    response=make_response(image_data)
    response.header['Content-Type']='image/jpg'
    return response