from .WXBizDataCrypt import WXBizDataCrypt
import time


class WechatSteps:
    def __init__(self, session_key):
        self.session_key = session_key
        self.crypt = WXBizDataCrypt(session_key)

    def get_data(self, iv, encrypted_data):

        class RunInfo:
            def __init__(self, data):
                self.raw_data = data
                self.last_day_steps = data['stepInfoList'][-1]['step']
                self.timestamp = data['watermark']['timestamp']
        return RunInfo(self.crypt.decrypt(encrypted_data, iv))

    def update_data(self, iv, encrypted_data, new_steps):
        data = self.crypt.decrypt(encrypted_data, iv)
        data['stepInfoList'][-1]['step'] = new_steps
        data['watermark']['timestamp'] = int(time.time())
        data = self.crypt.encrypt(data, iv)
        return data
