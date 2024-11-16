import socket 


hostname = socket.gethostname()

myip = socket.gethostbyname(hostname)

print('my ip address is ' + myip)
