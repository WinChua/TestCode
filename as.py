import socket
import select
import time
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12346))
server.listen(1024)
def dealcli(cli, addr):
    # print "recv", addr
    data = cli.recv(1024)
    time.sleep(0.1)
    cli.send("hello")
    # print "send", addr


while True:
    cli, addr = server.accept()
    # print "get", addr
    t = Thread(target=dealcli, args=(cli, addr))
    t.start()
