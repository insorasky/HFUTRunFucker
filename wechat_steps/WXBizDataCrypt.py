import base64
import json
from Crypto.Cipher import AES


class WXBizDataCrypt:
    __BLOCK_SIZE_16 = BLOCK_SIZE_16 = AES.block_size

    def __init__(self, sessionKey):
        self.sessionKey = sessionKey

    def decrypt(self, encryptedData, iv):
        # base64 decode
        sessionKey = base64.b64decode(self.sessionKey)
        encryptedData = base64.b64decode(encryptedData)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        decrypted = json.loads(self._unpad(cipher.decrypt(encryptedData)))
        return decrypted

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def _pad(self, text):
        length = AES.block_size
        count = len(text.encode('utf-8'))
        add = length - (count % length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, data, iv):
        data = json.dumps(data, separators=(',', ':'))
        sessionKey = base64.b64decode(self.sessionKey)
        iv = base64.b64decode(iv)
        cipher = AES.new(sessionKey, AES.MODE_CBC, iv)
        msg = cipher.encrypt(self._pad(data).encode())
        msg = base64.b64encode(msg).decode()
        return msg
