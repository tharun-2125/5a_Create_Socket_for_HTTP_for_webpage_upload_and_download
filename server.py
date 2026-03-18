
import socket

def download_page(host, path):
    port = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    s.send(request.encode())

    response = s.recv(4096).decode()

    print("Server Response:\n")
    print(response)

    s.close()


host = "example.com"
path = "/"

download_page(host, path)