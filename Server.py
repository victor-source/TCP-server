
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

s.bind(('127.0.0.1', 12345))  

s.listen(5)  

while True:  

    connection,address = s.accept()  

    conn = conn.recv(1024)  

    print(con)

    conn.send(conn)    		    connection.close()
