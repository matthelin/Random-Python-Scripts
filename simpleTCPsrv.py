#!/usr/bin/python

# Matt Helin 2018
# This is a basic TCP listener written in Python

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpSocket.bind(("0.0.0.0", 8080))

tcpSocket.listen(2)

#Below, client is the varible for the accept, ip is ip, port is port
(client, (ip,port)) = tcpSocket.accept()

print ("Connection received from %s on port %s" % (ip,port))

client.send("Welcome! ")

# You can also receive data from the client
# data = client.recv(2048)
# data sets the variable, client is the accept variable earlier
# the recv sub-function sets the buffer size