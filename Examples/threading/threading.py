
import threading

def run_thread1():
    while(True):
        pass

def run_thread2():
    while(True):
        pass

if __name__ == '__main__':
    
    thread_1 = threading.Thread(target= run_thread1, args =())
    thread_1.setDaemon(True)
    thread_1.start()

    thread_2 = threading.Thread(target= run_thread2, args =())
    thread_2.setDaemon(True)
    thread_2.start()

    ## Stop main thread, wait the thread to finish
    # thread_1.join()
    # thread_2.join()

    while True:
        pass