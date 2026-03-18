import socket

def upload_file(host, port, filename):

    with open(filename, "rb") as file:
        data = file.read()

    content_length = len(data)

    request = (
        f"POST /upload HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Content-Length: {content_length}\r\n\r\n"
    )

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.send(request.encode() + data)

    response = s.recv(4096).decode()
    print(response)

    s.close()


host = "example.com"
port = 80
filename = "example.txt"

upload_file(host, port, filename)