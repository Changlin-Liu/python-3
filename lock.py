import time, threading, random

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    print(balance)
    balance = balance - n
    print(balance)
    time.sleep(random.random() * 2)

def run_thread(n):
    for i in range(10):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('final balance is %d' % balance)
