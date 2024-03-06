import time as t  # Importing the time module for measuring execution time
import threading  # Importing the threading module for multi-threading
from concurrent.futures import ThreadPoolExecutor  # Importing ThreadPoolExecutor for thread pool concurrency

# Function to simulate a time-consuming task
def Func(n):
    print("Thread: " + str(n))
    t.sleep(3)  # Simulating a delay of 3 seconds
    return

# Manually invoking the function without threading
T = t.time()  # Start time
print("***** START *****")

# Invoking the function sequentially for different threads without threading
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

# Threads without join
T = t.time()  # Start time
print("***** START *****")

# Creating threads and starting them without using join
T1 = t.time()
Thread1 = threading.Thread(target=Func, args=[1])
print(f"Thread T1: time: {t.time() - T1}")
T2 = t.time()
Thread2 = threading.Thread(target=Func, args=[2])
print(f"Thread T2: time: {t.time() - T2}")
T3 = t.time()
Thread3 = threading.Thread(target=Func, args=[3])
print(f"Thread T3: time: {t.time() - T3}")
T4 = t.time()
Thread4 = threading.Thread(target=Func, args=[4])
print(f"Thread T4: time: {t.time() - T4}")

print(f"Program Time: {t.time() - T}")
print("***** END *****")

# Threads with join
T = t.time()  # Start time
print("***** START *****")

# Creating threads and starting them with join
T1 = t.time()
Thread1 = threading.Thread(target=Func, args=[1])
print(f"Thread T1: time: {t.time() - T1}")
T2 = t.time()
Thread2 = threading.Thread(target=Func, args=[2])
print(f"Thread T2: time: {t.time() - T2}")
T3 = t.time()
Thread3 = threading.Thread(target=Func, args=[3])
print(f"Thread T3: time: {t.time() - T3}")
T4 = t.time()
Thread4 = threading.Thread(target=Func, args=[4])
print(f"Thread T4: time: {t.time() - T4}")

# Starting threads
Thread1.start()
Thread2.start()
Thread3.start()
Thread4.start()

# Waiting for threads to finish
Thread1.join()
Thread2.join()
Thread3.join()
Thread4.join()

print(f"Program Time: {t.time() - T}")
print("***** END *****")

# Thread pool concurrent - manually
T = t.time()  # Start time
print("***** START *****")

# Using ThreadPoolExecutor to execute tasks manually
with ThreadPoolExecutor(max_workers=4) as executor:
    Ft11 = t.time()
    Ft1 = executor.submit(Func, 1)
    Ft12 = t.time()
    Ft2 = executor.submit(Func, 2)
    Ft13 = t.time()
    Ft3 = executor.submit(Func, 3)
    Ft14 = t.time()
    Ft4 = executor.submit(Func, 4)

    print(f"Ft1: {Ft1}: time {t.time() - Ft11}")
    print(f"Ft2: {Ft2}: time {t.time() - Ft12}")
    print(f"Ft3: {Ft3}: time {t.time() - Ft13}")
    print(f"Ft4: {Ft4}: time {t.time() - Ft14}")

print(f"Program Time: {t.time() - T}")
print("***** END *****")

# Thread pool concurrent - with List
T = t.time()  # Start time
print("***** START *****")

# Using ThreadPoolExecutor with a list of tasks
with ThreadPoolExecutor(max_workers=4) as executor:
    l = [1, 2, 3, 4]
    results = executor.map(Func, l)
    for result in results:
        print(result)

print(f"Program Time: {t.time() - T}")
print("***** END *****")
