```
class Process:
  def __init__ (self, name, arrival_time, burst_time, priority=None):
    self.name = name
    self.arrival_time = arrival_time
    self.burst_time = burst_time
    self.priority = priority

  def __str__ (self):
    return f"{self.name} | Arrival Time: {self.arrival_time} | Burst Time: {self.burst_time} | Priority: {self.priority}"

#FIFO
def scheduler(processes):
    processes.sort(key=lambda p: p.arrival_time)
    current_time = 9
    total_waiting_time = 0
    completed_processes = 0

    for process in processes:
      if process.arrival_time > current_time:
        current_time = process.arrival_time
      waiting_time = current_time - process.arrival_time
      total_waiting_time += waiting_time
      current_time += process.burst_time
      completed_processes += 1
      if completed_processes == 500:
        break

    #calculations
    avg_waiting_time = total_waiting_time / len(processes[:completed_processes])
    throughput = completed_processes / current_time
    cpu_utl = sum(p.burst_time for p in processes[:completed_processes]) / current_time
    avg_turnaround_time = current_time / completed_processes
    avg_response_time = avg_waiting_time

    #output
    print("\nStatistics for the run:")
    print(f"Number of processes: {completed_processes}")
    print(f"Total elapsed time (for the scheduler): {current_time}")
    print(f"Throughput: {throughput:.2f}")
    print(f"CPU Utilization: {cpu_utl:.2%}")
    print(f"Average waiting time (in CPU burst times): {avg_waiting_time:.2f}")
    print(f"Average turnaround time (in CPU burst times): {avg_turnaround_time:.2f}")
    print(f"Average response time (in CPU burst times): {avg_response_time:.2f}")

#read in data
def read_data(filepath):
    processes = []
    with open(filepath, 'r') as file:
      for line in file:
        data = line.strip().split()
        if len(data) == 3:
          arrival_time, burst_time, priority = map(int, data)
          process = Process("", arrival_time, burst_time, priority)
          processes.append(process)
    return processes

#execution
filepath = '/content/datafile1-txt.txt'
print("FIFO:")
processes = read_data(filepath)
scheduler(processes)
```
