from mitmproxy.http import HTTPFlow
from wechat_steps import WechatSteps
import json
from .session import session


class CatchToken:
    session_key = ''
    student_id = 0
    account = ''
    task_id = 0
    wechat_steps_data = ''
    wechat_steps_iv = ''
    wechat_steps = ''
    headers = {}

    def response(self, flow: HTTPFlow):
        url = flow.request.pretty_url
        if 'https://tiyun.yzhiee.com/wxlogin?code=' in url:
            data = json.loads(flow.response.content)
            self.session_key = data['data']['sessionKey']
            self.student_id = data['data']['studentId']
            self.account = data['data']['account']
            self.wechat_steps = WechatSteps(self.session_key)
            print('检测到小程序登录请求，SessionKey：%s；用户ID：%s；学工号：%s；Token：%s' %
                  (self.session_key, self.student_id, self.account, data['data']['token']))
        elif 'https://tiyun.yzhiee.com/run/task' in url:
            data = json.loads(flow.response.content)
            self.task_id = data['data']['id']
            print('检测到任务获取请求，任务名称：%s；任务ID：%s' % (data['data']['name'], self.task_id))
        elif 'https://tiyun.yzhiee.com/wx/steps' in url:
            data = json.loads(flow.request.content)
            self.wechat_steps_data = data['encryptedData']
            self.wechat_steps_iv = data['iv']
            for header in flow.request.headers:
                self.headers[header] = flow.request.headers[header]
            self.wechat_steps_old = self.wechat_steps.get_data(self.wechat_steps_iv, self.wechat_steps_data).last_day_steps
            print('检测到微信步数请求，今日步数：%s' % self.wechat_steps_old)
            session(self)
