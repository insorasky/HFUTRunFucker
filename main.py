from mitmdump import DumpMaster, Options
from addon import *
from onboardingapp import app
from mitmproxy.addons import asgiapp
from mitmproxy.certs import CertStore
import os

addons = [
    CatchToken(),
    Client(),
    asgiapp.WSGIApp(app, 'run.sorasky.in', 80)
]

if __name__ == '__main__':
    print("""欢迎使用HFUTRunFucker！
Sora 版权所有 https://www.sorasky.in/
本人仅提供工具，所有通过本工具所进行的行为都与本人无关，后果由使用者自负，敬请周知！
如果您使用电脑（建议），请在电脑的代理设置界面设置代理，方法请见 https://github.com/insorasky/HFUTRunFucker/；
如果您使用手机，请在手机和电脑连接同一网络后，将手机HTTP代理端口号设为10086，IP为电脑局域网内地址，方法请百度；
如果是第一次使用，请用设备浏览器打开：run.sorasky.in，根据指示安装证书！
使用方法：在代理环境下打开健跑微信小程序（如果您使用电脑，可通过点击手机分享给电脑的小程序卡片打开小程序），切换到开始跑步页面（不要点击开始跑步），系统会自动处理！""")

    if not os.path.exists('./certs'):
        CertStore.create_store(
            path=os.path.abspath('./certs'),
            basename='mitmproxy',
            key_size=2048,
            organization='HFUTRunFucker',
            cn='HFUTRunFucker'
        )

    options = Options(
        listen_port=10086,
        scripts=__file__,
        termlog_verbosity='error',
        onboarding=False,
        confdir=os.path.abspath('./certs')
    )
    dm = DumpMaster(options)
    dm.run()
