from flask import request, jsonify, current_app
from info.utils.captcha.captcha import captcha
from info.utils import RET
from . import passport_blu
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
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR,errmsg='验证码操作失败')