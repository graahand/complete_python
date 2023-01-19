import socket

def network_info():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Hostname: ",hostname)
    print("IP Address: ",IPAddr)

network_info()
