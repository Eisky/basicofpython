import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print('New Conn:', self.client_address)
            data = self.request.recv(1024)
            if not data:
                break
            self.request.send(data)


if __name__ == '__main__':
    HOST, PORT = 'localhost', 50007

    # 把刚才写的类当作一个参数传递给ThreadingTCPserver这个类，下面的代码就
    # 创建了一个多线程socket server

server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

server.serve_forever()
