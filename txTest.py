import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 7331

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

print('tx test')

while True:
    msg = '1000110110101010000100010010001001011000100110111000010110000000000000000100000000000000000011000100101101110101'
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.5)
    msg = '1000110110101010000100010010001001011000100110111000001000000000000000001000000000000000100000010110001001001110'
    sock.sendto(msg.encode(), (UDP_IP, UDP_PORT))
    time.sleep(0.5)