from threading import Thread
import time


def first():
    print("First Thread")
    time.sleep(1)  # Simulate a delay


def second():
    print("Second Thread")
    time.sleep(1)  # Simulate a delay


def third():
    print("Third Thread")
    time.sleep(1)  # Simulate a delay


if __name__ == '__main__':
    start_time = time.time()

    t1 = Thread(target=first)
    t1.start()
    t2 = Thread(target=second)
    t2.start()
    t3 = Thread(target=third)
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print(f"Total time taken: {time.time() - start_time} seconds")
