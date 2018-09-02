import threading
import socket
import time
import click
import datetime

def senddata():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 12346))
    sock.send("hello")
    sock.recv(10)
    sock.close()

sleeptime = 20

def sleepfunc():
    time.sleep(sleeptime)

@click.group()
def cli():
    pass

@cli.command()
@click.option("--times", default=100, help="test time")
@click.option("--sleeps", default=0, help="test sleep")
@click.option("--nostart", default=False, help="no start")
def thread(times, sleeps, nostart):
    start = datetime.datetime.now()
    threads = []
    # target = senddata if not sleeps else sleepfunc
    target = senddata
    if sleeps:
        global sleeptime
        sleeptime = sleeps
    for i in range(times):
        t = threading.Thread(target=target)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = datetime.datetime.now()
    print "run %d times, cost %f" %(times, (end - start).total_seconds())

@cli.command()
@click.option("--times", default=100, help="test time")
def seq(times):
    start = datetime.datetime.now()
    for i in range(times):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 12346))
        sock.send("hello")
        sock.recv(10)
        sock.close()
    end = datetime.datetime.now()
    print "seq times %d, cost %f" % (times, (end-start).total_seconds())

if __name__ == "__main__":
    cli()
