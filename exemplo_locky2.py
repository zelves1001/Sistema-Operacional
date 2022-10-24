import threading
import time
import random

g = 0
lock = threading.Lock()

def incrementa():
    global g
    lock.acquire()
    tmp = g     # le valor
    time.sleep(random.randint(0,1))
    tmp += 1    # incrementa
    g = tmp     # escreve
    lock.release()

if __name__=="__main__":
    thread1 = threading.Thread(target=incrementa, args = ())
    thread1.start()

    thread2 = threading.Thread(target=incrementa, args = ())
    thread2.start()

    thread1.join()
    thread2.join()

    print(g)