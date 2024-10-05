import threading
import time

def worker():
    print("Worker thread started")
    while True:
        print("Working...")
        time.sleep(1)

def monitor_thread(target_thread, timeout):
    last_active_time = time.time()
    while target_thread.is_alive():
        if time.time() - last_active_time > timeout:
            print("Target thread is stuck!")
            # You can take further action here, like terminating the stuck thread
            break
        print("Monitoring thread...")
        time.sleep(2)

if __name__ == "__main__":
    # Create the worker thread
    t = threading.Thread(target=worker)

    # Start the worker thread
    t.start()

    # Set the timeout for monitoring
    timeout = 5  # seconds

    # Create and start the monitoring thread
    monitor_t = threading.Thread(target=monitor_thread, args=(t, timeout))
    monitor_t.start()

    # Wait for both threads to finish (which won't happen in this example)
    t.join()
    monitor_t.join()
