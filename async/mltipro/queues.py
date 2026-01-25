from multiprocessing import Process, Queue
import os
import time

# task for writing process


def write(q):
    print(f'Writing Process ID: {os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'Write {value} to the queue.')
        q.put(value)

# task for reading process


def read(q):
    print(f'Reading Process ID: {os.getpid()}')
    while True:
        if q.empty():
            break
        else:
            value = q.get(True)
            print(f'Read {value} from the queue.')


if __name__ == '__main__':
    start = time.time()
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # the process pw is to write data to Queue:
    pw.start()
    # the process pr is to read data from Queue:
    pr.start()

    pw.join()
    pr.join()
    print(f'Total time taken: {time.time() - start} seconds')
