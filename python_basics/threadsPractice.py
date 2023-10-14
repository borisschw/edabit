import threading
import time

def run(data, stop):
    while True:
        print(data)
        time.sleep(1)
        if stop():
                break

def main():
        stop_threads = False
        t1 = threading.Thread(target = run, args =("hello", lambda : stop_threads, ))
        t1.start()
        time.sleep(1)
        stop_threads = True
        # t1.join()
        print('thread killed')
main()