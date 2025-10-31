import threading
import time

# def producer(condition):
#     pass

# def consumer(condition):
#     pass

# def writer(condition):
#     pass

# def reader(condition):
#     pass

def write_data(condition):
    condition.acquire()
    with open("data.txt", "w") as file:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for day in days:
            temp = float(input(f"Enter temperature for {day}: "))
            file.write(f"{day}: {temp}\n")
    condition.notify_all()
    condition.release()

def max_temp(condition):
   condition.acquire()
   condition.wait(timeout=1)
   with open("data.txt", "r") as file:
       data = file.readlines()
       max_temp = float(data[0].split(":")[1])
       for line in data:
           if float(line.split(":")[1]) > max_temp:
               max_temp = float(line.split(":")[1])
       print(f"Maximum temperature: {max_temp}")
   condition.release()

def avg_temp(condition):
   condition.acquire()
   condition.wait(timeout=1)
   with open("data.txt", "r") as file:
       data = file.readlines()
       total = 0
       for line in data:
           total += float(line.split(":")[1])
       avg = total / len(data)
       print(f"Average temperature: {avg}")
   condition.release()

condition = threading.Condition()

write_thread = threading.Thread(target=write_data, args=(condition,))
max_thread = threading.Thread(target=max_temp, args=(condition,))
avg_thread = threading.Thread(target=avg_temp, args=(condition,))

write_thread.run()
max_thread.run()
avg_thread.run()



