from vidstream import StreamingServer #pip install vidstream
import threading

filepath=r'config.txt'
f=open(filepath,"r")
ip_r = f.readline()
f.close

#my ip = "192.168.1.100"
print(ip_r)

reviver = StreamingServer(ip_r, 9999)

t = threading.Thread(target=reviver.start_server)
t.start()