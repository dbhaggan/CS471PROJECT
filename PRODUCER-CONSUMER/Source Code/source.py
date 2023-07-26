```
import threading
import time
import random
from queue import Queue

BUFFER_SIZE = 10

buffer = Queue(BUFFER_SIZE)
items_produced = 0
items_consumed = 0

def producer(p_id):
  global items_produced
  while True:
    item = items_produced + 1
    if buffer.full():
      print(f"Producer {p_id} waiting...")
    buffer.put(item)
    print(f"Producer {p_id} produced item {item} ")
    items_produced = item
    time.sleep(random.random() + 0.5)

def consumer(c_id):
  global items_consumed
  while True:
    if buffer.empty():
      print(f"Consumer {c_id} waiting...")
    item = buffer.get()
    print(f"Consumer {c_id} consumed item {item} ")
    items_consumed += 1
    buffer.task_done()
    time.sleep(random.random() * 0.5)

def main(num_producers, num_consumers, sleep_Time):
  producers = []
  consumers = []

  for i in range(num_producers):
    producer_thread = threading.Thread(target=producer, args=(i + 1,))
    producers.append(producer_thread)
    producer_thread.start()

  for i in range(num_consumers):
    consumer_thread = threading.Thread(target=consumer, args=(i + 1,))
    consumers.append(consumer_thread)
    consumer_thread.start()

  time.sleep(sleep_time)

  for producer_thread in producers:
    producer_thread.join()

  for consumer_thread in consumers:
    consumer_thread.join()

  print("Test Case | Number of Prodcuers | Number of Consumers | Turnaround Time")
  print("-----------------------------------------------------------------")
  print(f"   1       {num_producers}        {num_consumers}")

if __name__ == "__main__":
  num_producers = 4
  num_consumers = 2
  sleep_time = 5
  main(num_producers, num_consumers, sleep_time)
```
