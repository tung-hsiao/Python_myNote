import threading
from queue import Queue

def thread_job(data, q):
    q.put(data)

if __name__ == '__main__':
    data = [[1, 2, 3], [4, 5, 6]]
    q = Queue()

    thread_1 = threading.Thread(target=thread_job, args=([1, 2, 3], q))
    thread_2 = threading.Thread(target=thread_job, args=([4, 5, 6], q))
          
    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    result = []
    for _ in range(q.qsize()):
        result.append(q.get())
    print(result)