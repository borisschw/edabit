import queue

# Create a Queue with a maximum size of 5
q = queue.Queue(maxsize=10)

# Adding elements to the queue
for i in range(13):
    q.put(f"Item {i}")

# Trying to add another item will block until there is space unless used with put_nowait
try:
    q.put_nowait("Item 5")  # Raises queue.Full if the queue is full
except queue.Full:
    print("Queue is full, cannot add 'Item 5'")
