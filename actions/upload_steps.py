from requests import post
from wechat_steps import WechatSteps


def upload_steps(headers, session_key, encrypted_data, iv, new_steps):
    steps = WechatSteps(session_key)
    encrypted_data = steps.update_data(iv, encrypted_data, new_steps)
    data = post('https://tiyun.yzhiee.com/wx/steps',
                json={
                    'encryptedData': encrypted_data,
                    'iv': iv
                }, headers=headers).json()
    return data['message'] == 'success'
