import time
import _thread
import threading


def work1():
    print("task 1 begin: ", time.ctime())
    time.sleep(4)
    print("task 1 end: ", time.ctime())


def work2():
    print("task 2 begin: ", time.ctime())
    time.sleep(2)
    print("task 2 end: ", time.ctime())


def main():
    print("main begin:", time.ctime())
    _thread.start_new_thread(work1, ())
    _thread.start_new_thread(work2, ())
    print("main end:", time.ctime())

    for i in range(20):
        time.sleep(1)


def work21(in1):
    print("任务1开始啦：{0}\n".format(time.ctime()))
    print("我是参数", in1)
    time.sleep(4)
    print("任务1结束了：{0}".format(time.ctime()))


def work22(in1,in2):
    print("任务2开始啦：{0}\n".format(time.ctime()))
    print("我是参数",in1,in2)
    time.sleep(2)
    print("任务2结束了：{0}".format(time.ctime()))


def main2():
    print("主程序开始啦：{0}".format(time.ctime()));
    # 创建子线程
    t1 = threading.Thread(target=work1, args=("二狗子",));
    t2 = threading.Thread(target=work2, args=("傻子", "大笨蛋"));

    # 启动子线程
    t1.start();
    t2.start();

    # 等子线程执行完毕再退出
    t1.join();
    t2.join();
    print("主程序结束了：{0}".format(time.ctime()));


class mythread(threading.Thread):
    def __init__(self, arg):
        threading.Thread.__init__(self)
        self.arg = arg

    def run(self):
        time.sleep(2)
        print(self.arg)


for i in range(5):
    t = mythread(i)
    t.start()
    #t.join()

print("主线程执行完毕！")