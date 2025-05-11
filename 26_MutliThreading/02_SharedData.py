# import threading

# counter = 0

# lock = threading.Lock()
# def increment_counter_with_lock():
#     global counter
#     for _ in range(100000):
#         # Simulate some work with a sleep
#         threading.Event().wait(0.0001)
#         with lock:
#             counter += 1

# thread1 = threading.Thread(target=increment_counter_with_lock, args=("Thread 1",))
# thread2 = threading.Thread(target=increment_counter_with_lock, args=("Thread 2",))

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for threads to complete
# thread1.join()
# thread2.join()

# print(f"Final counter value: {counter}")

from threading import Lock, Thread

lock = Lock()
shared_data = 0

def increment():
    global shared_data
    with lock:
        shared_data += 1

threads = [Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(shared_data) 