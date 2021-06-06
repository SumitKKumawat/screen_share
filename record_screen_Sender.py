from vidstream import ScreenShareClient
import threading

filepath=r'config.txt'
f=open(filepath,"r")
ip_r = f.readline()
f.close

#my ip = "192.168.1.100"
print(ip_r)

sender = ScreenShareClient(ip_r, 9999)

t = threading.Thread(target=sender.start_stream)
t.start()