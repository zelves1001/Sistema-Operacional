import threading
deposit = 100
trava = threading.Lock()
# Function to add profit to the deposit
def add_profit():
    global deposit
    for i in range(1000000):
        trava.acquire()
        deposit = deposit + 10
        trava.release()
# Function to deduct money from the deposit
def pay_bill():
    global deposit
    for i in range(1000000):
        trava.acquire()
        deposit = deposit - 10
        trava.release()
# Creating threads
thread1 = threading.Thread(target = add_profit, args = ())
thread2 = threading.Thread(target = pay_bill, args = ())
thread3 = threading.Thread(target = add_profit, args = ())
# Starting the threads
thread1.start()
thread2.start()
thread3.start()
# Waiting for both the threads to finish executing
thread1.join()
thread2.join()
thread3.join()
# Displaying the final value of the deposit
print(deposit)