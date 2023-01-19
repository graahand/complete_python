import psutil
import time

def network_speed():
    initial_bytes_sent = psutil.net_io_counters().bytes_sent
    initial_bytes_recv = psutil.net_io_counters().bytes_recv
    time.sleep(1) # wait for 1 second
    final_bytes_sent = psutil.net_io_counters().bytes_sent
    final_bytes_recv = psutil.net_io_counters().bytes_recv
    sent_speed = (final_bytes_sent - initial_bytes_sent) / 1024 # convert to KB
    recv_speed = (final_bytes_recv - initial_bytes_recv) / 1024 # convert to KB
    print("Upload speed: {} KB/s".format(sent_speed))
    print("Download speed: {} KB/s".format(recv_speed))

while True:
    network_speed()
    
