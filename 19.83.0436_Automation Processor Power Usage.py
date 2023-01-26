import psutil
import time

def monitor():
    while True:
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        print("CPU Usage: ", cpu_usage)
        print("Memory Usage: ", mem_usage)
        print("Disk Usage: ", disk_usage)
        print("-------------------------------")
        print("Proses Konsumsi CPU:")
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            if proc.info['cpu_percent'] is not None:
                print(proc.info)
        print("-------------------------------")
        print("Proses Konsumsi Memori:")
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            mem = proc.info['memory_info']
            if mem is not None:
                print(proc.info)
        time.sleep(1)

# start the monitoring
monitor()
