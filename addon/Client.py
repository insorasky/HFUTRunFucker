import mitmproxy.proxy.protocol


class Client:
    connect_noticed = False

    def clientconnect(self, layer: mitmproxy.proxy.protocol.Layer):
        if self.connect_noticed is False:
            print("有设备连接！")
            self.connect_noticed = True
