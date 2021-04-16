from mitmdump import DumpMaster, Options
from addon import *

addons = [
    CatchToken(),
    Client(),
]

if __name__ == '__main__':
    print("""欢迎使用HFUTRunFucker！
Sora 版权所有 https://www.sorasky.in/
本人仅提供工具，所有通过本工具所进行的行为都与本人无关，后果由使用者自负，敬请周知！
请在手机和电脑连接同一网络后，将手机HTTP代理端口号设为10086，IP为电脑局域网内地址，方法请百度；
如果是第一次使用，请用手机浏览器打开：mitm.it，根据指示安装证书！
使用方法：在代理环境下打开健跑微信小程序，切换到开始跑步页面（不要点击开始跑步），系统会自动处理！
为以防万一，使用本工具后，今日内请不要再打开小程序！""")

    options = Options(listen_port=10086, scripts=__file__, onboarding_host='hfut.run', termlog_verbosity='error')
    dm = DumpMaster(options)
    dm.run()
