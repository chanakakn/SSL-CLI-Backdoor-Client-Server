from OpenSSL import SSL
import socket
import sys

HOST = '192.168.0.200'
PORT = 31337
ADDRESS = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.use_certificate_file('server.crt')
sslSock = SSL.Connection(ctx, sock)
sslSock.connect(ADDRESS)

def main():
    try:
        cmd = input('$ ')
        sslSock.sendall(cmd.encode())
        data = sslSock.recv(66384).decode()
        print(data)
    except KeyboardInterrupt:
        sslSock.close()
        sys.exit(0)

while True:
    main()
