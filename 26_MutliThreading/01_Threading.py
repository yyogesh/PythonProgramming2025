import threading

def print_numbers():
    for i in range(1, 6):
        print(i)
        # Simulate some work with a sleep
        threading.Event().wait(0.5)


thread1 = threading.Thread(target=print_numbers, name="Thread-1")
thread2 = threading.Thread(target=print_numbers, name="Thread-2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished execution.")