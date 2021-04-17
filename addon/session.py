from actions import *
import time
from mitmproxy import ctx


def session(catch_token):
    if catch_token.session_key and catch_token.student_id and catch_token.account and catch_token.task_id and 'catch_token.wechat_steps' and catch_token.headers:
        choice = input("数据获取完毕，是否继续？(y/N)")
        if choice == 'Y' or choice == 'y':
            print("提交开始请求")
            score_id = start(catch_token.headers, catch_token.task_id, catch_token.student_id)
            if score_id:
                start_time = time.time()
                print('成功开始跑步任务，任务编号：%s' % score_id)
                print('请立即关闭小程序（方法：在最近任务界面划掉小程序，如果不显示单独小程序则请关闭微信）！')
                print('现在可以将代理改为默认设置以免无法上网！')
                input("请在要结束时回车继续！建议每次挂1.5小时以内以免登录凭证过期：")
                total_time = time.time() - start_time
                distance = format(total_time * 0.002, '.2f')
                finished = finish(catch_token.headers, score_id, catch_token.account, catch_token.student_id, distance)
                if finished:
                    print('提交距离请求成功！本次您刷了%skm' % distance)
                    '''
                    steps = int(total_time * 1.6)
                    uploaded = upload_steps(catch_token.headers, catch_token.session_key, catch_token.wechat_steps_data,
                                            catch_token.wechat_steps_iv, catch_token.wechat_steps_old + steps)
                    if uploaded:
                        print('提交步数请求成功！本次您刷了%s步' % steps)
                    else:
                        print('提交步数请求失败！')
                    '''
                    input('本次刷步完成！按回车键退出。')
                    ctx.master.shutdown()
            else:
                print("提交开始请求失败！")
    else:
        print("数据不完整，请右上角菜单——重启小程序后重新操作！")
