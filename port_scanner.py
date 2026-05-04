import socket
import time
import threading


start_time=time.time()
target = input("Enter target ip address or Domain Name :-")

target_ip = socket.gethostbyname(target)
print("Resolved Ip :- ",target_ip)

ports = range(1,101)
open_ports = []

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result=s.connect_ex((target_ip, port))

    if result == 0:
        open_ports.append(port)
        try: 
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print(f"[OPEN] Port {port:<5} Service: {service}")
    
    s.close()

threads = []

for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan is Complete")
print(f"Open Ports: {open_ports}")

end_time = time.time()
print(f"Time taken : {end_time - start_time:.2f} seconds")