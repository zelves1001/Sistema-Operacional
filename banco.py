from concurrent.futures import thread
from pydoc import cli
import time
import random
import threading

semaforo = threading.Semaphore(3)

clientes = []

for i in range(30):
    print(i)
    clientes.append(i)

def atendimento():
    for i in clientes:
        semaforo.acquire()
        print("Caixa " + threading.currentThread().getName() + " esta atendendo cliente " + str(i))
        clientes.remove(i)
        time.sleep(random.randint(0,1))
        semaforo.release()

thread1 = threading.Thread(target = atendimento, args = ())
thread2 = threading.Thread(target = atendimento, args = ())
thread3 = threading.Thread(target = atendimento, args = ())

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

#print(clientes)