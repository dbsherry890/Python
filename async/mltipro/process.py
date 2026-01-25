from multiprocessing import Process
import os


def print_square(num):
    print(f'Run child process {os.getpid()}')
    print(f"Square: {num * num}")


if __name__ == '__main__':
    print(f'Parent process {os.getpid()}')
    p = Process(target=print_square, args=(5,))
    p.start()
    p.join()
