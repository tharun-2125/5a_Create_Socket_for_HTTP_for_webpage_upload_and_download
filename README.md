# 5a_Create_Socket_for_HTTP_for_webpage_upload_and_download
## AIM :
To write a PYTHON program for socket for HTTP for web page upload and download
## Algorithm

1.Start the program.
<BR>
2.Get the frame size from the user
<BR>
3.To create the frame based on the user request.
<BR>
4.To send frames to server from the client side.
<BR>
5.If your frames reach the server it will send ACK signal to client otherwise it will send NACK signal to client.
<BR>
6.Stop the program
<BR>

## Program 
## client.py
~~~
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
~~~

## server.py
~~~

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
~~~
## OUTPUT
![alt text](<Screenshot 2026-03-18 113326.png>) ![alt text](<Screenshot 2026-03-18 113343.png>)

## Result
Thus the socket for HTTP for web page upload and download created and Executed
