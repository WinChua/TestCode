import socket
import select
import time
from threading import Thread
import asyncio

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12346))
server.listen(1024)
@asyncio.coroutine
def dealcli(cli, addr):
    # print "recv", addr
    data = cli.recv(1024)
    yield from asyncio.sleep(0.1)
    cli.send("hello")
    # print "send", addr

@asyncio.coroutine
def main():
    while True:
        cli, addr = server.accept()
        # print "get", addr
        yield from dealcli(cli,addr)
