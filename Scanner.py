import socket

def check(ip,port):
    s=socket.socket()
    s.connect((ip,port))
    banner=s.recv(1024)
    return banner


def checkVuln(banner):
    if 'FTP float server version(1.0.0)' in banner:
        print('server might be at risk')
    elif 'Apache 2.34 ' in banner:
        print('server might be at risk')
    

def main():
    ports=[21,22,25,143,445]
    for i in range(1,255):
        ip='x.x.x.'+str(i)
        for port in ports:
            banner=check(ip,port)
            if banner:
                checkVuln(banner)

if __name__=='__main__':
    main()