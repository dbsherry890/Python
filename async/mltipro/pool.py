from multiprocessing import Pool
import time

def square(num):
    print(f"Square: {num * num}")
    time.sleep(1) 

if __name__ == "__main__":
    start_time = time.time()
    with Pool(4) as pool:
        pool.map(square, [1, 2, 3, 4])
    print(
        f"Multiprocessing Execution Time: {time.time() - start_time} seconds")

    # Returns:
        # Square: 1 Square: 4
        # Square: 9
        # Square: 16
        # Multiprocessing Execution Time: 1.0998249053955078 seconds
