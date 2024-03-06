import time as t  
# Importing the time module to measure execution time
import multiprocessing  
# Importing the multiprocessing module for parallel processing
from concurrent.futures import ProcessPoolExecutor  
# Importing ProcessPoolExecutor for concurrent processing

# Function to simulate a time-consuming task
def Func(n):
    print("Thread: " + str(n))
    t.sleep(3)  # Simulating a delay of 3 seconds
    return

# Manually invoking the function without multiprocessing
def manually():
    T = t.time()  # Start time
    print("***** START *****")

    # Invoking the function sequentially for different threads
    T1 = t.time()
    Func(1)
    print(f"Thread T1: time: {t.time() - T1}")
    T2 = t.time()
    Func(2)
    print(f"Thread T2: time: {t.time() - T2}")
    T3 = t.time()
    Func(3)
    print(f"Thread T3: time: {t.time() - T3}")
    T4 = t.time()
    Func(4)
    print(f"Thread T4: time: {t.time() - T4}")

    print(f"Program Time: {t.time() - T}")
    print("***** END *****")

# Multi-processing version 1
def multiprocessingversion1():
    if __name__ == "__main__":
        print("***** START *****")
        T = t.time()  # Start time
        mpt1 = t.time()
        MP1 = multiprocessing.Process(target=Func, args=[1])  # Creating a process
        MP1.start()  # Starting the process
        MP1.join()  # Waiting for the process to finish
        print(f"Time: {t.time() - mpt1}")  # Time taken for the first process
        mpt2 = t.time()
        MP2 = multiprocessing.Process(target=Func, args=[2])
        MP2.start()
        MP2.join()
        print(f"Time: {t.time() - mpt2}")
        mpt3 = t.time()
        MP3 = multiprocessing.Process(target=Func, args=[3])
        MP3.start()
        MP3.join()
        print(f"Time: {t.time() - mpt3}")

        print(f"Program Time: {t.time() - T}")
        print("***** END *****")

# Multi-processing version 2
def multiprocessingversion2():
    if __name__ == "__main__":
        print("***** START *****")
        T = t.time()  # Start time
        mpt1 = t.time()
        MP1 = multiprocessing.Process(target=Func, args=[1])
        print(f"Time: {t.time() - mpt1}")
        mpt2 = t.time()
        MP2 = multiprocessing.Process(target=Func, args=[2])
        print(f"Time: {t.time() - mpt2}")
        mpt3 = t.time()
        MP3 = multiprocessing.Process(target=Func, args=[3])
        print(f"Time: {t.time() - mpt3}")

        MP1.start()
        MP2.start()
        MP3.start()
        MP1.join()
        MP2.join()
        MP3.join()
        print(f"Program Time: {t.time() - T}")
        print("***** END *****")

# Concurrent features using ProcessPoolExecutor
def Concurrentfeatures():
    if __name__ == "__main__":
        print("***** START *****")
        T = t.time()  # Start time
        with ProcessPoolExecutor() as executor:
            # Mapping the function to multiple threads for concurrent execution
            results = executor.map(Func, [1, 2, 3, 4])
            for result in results:
                print(result)

        print(f"Program Time: {t.time() - T}")
        print("***** END *****")

# Invoking the functions and printing the results
print(f"def manually(): ")
manually()
print(f"def multiprocessingversion1(): ")
multiprocessingversion1()
print(f"def multiprocessingversion2(): ")
multiprocessingversion2()
print(f"def Concurrentfeatures(): ")
Concurrentfeatures()
