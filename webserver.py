#!/usr/bin/env python

"""
A simple echo server
"""

import socket
import sys
import os
import time
import threading
import select


def Head_Cont(a, file, type, b, status):  # to send header and content
    try:
        default = open("./document root directory" + file, "rb")
        defsend = default.read()
        size = os.stat("./document root directory" + file)
        sizeS = size.st_size
        if a[2] == "HTTP/1.1":
            header = a[2] + " " + status + "\n" + "Content-Type: " + \
                type + "\nContent-Length: " + \
                str(sizeS) + "\nConnection: " + b + "\n\n"
        else:
            header = a[2] + " " + status + "\n" + "Content-Type: " + \
                type + "\nContent-Length: " + str(sizeS) + "\n\n"
        headerB = header.encode()
        print(header)
        # print(defsend)
        #reply = headerB + defsend
        client.send(headerB)
        time.sleep(0.5)
        client.send(defsend)
    except:
        status = "404 Not Found"
        type = "text/html"
        file = "/404.html"
        b = "close"
        Head_Cont(a, file, type, b, status)


def GetData(a, b, Error):  # for GET request
    global Array
    if a[1] == "/" or a[1] == "/" + Array[2] or a[1] == "/" + Array[3] or a[1] == "/" + Array[4] or a[1] == "/" + Array[5]:
        # print("here")

        type = Array[7]
        file = "/" + Array[2]

        status = "200 OK"
        Head_Cont(a, file, type, b, status)

        # print(reply)
    else:
        check = a[1].split(".")
        n = len(check)
        try:
            print("In Try")
            if "." + check[n - 1] == Array[6]:
                type = Array[7]
                print("Extension supported")
            elif "." + check[n - 1] == Array[8]:
                type = Array[9]
                print("Extension supported")
            elif "." + check[n - 1] == Array[10]:
                type = Array[11]
                print("Extension supported")
            elif "." + check[n - 1] == Array[12]:
                type = Array[13]
                print("Extension supported")
            elif "." + check[n - 1] == Array[14]:
                type = Array[15]
                print("Extension supported")
            elif "." + check[n - 1] == Array[16]:
                type = Array[17]
                print("Extension supported")
            elif "." + check[n - 1] == Array[18]:
                type = Array[19]
                print("Extension supported")
            elif "." + check[n - 1] == Array[20]:
                type = Array[21]
                print("Extension supported")
            elif "." + check[n - 1] == Array[22]:
                type = Array[23]
                print("Extension supported")
            elif "." + check[n - 1] == Array[25]:
                type = Array[26]
                print("Extension supported")
            else:
                print("Error, extension not supported.")
                Error = 501
                status = "501 Not Implemented"
                file = "/501.html"
                type = "text/html"
                Head_Cont(a, file, type, b, status)

        except KeyboardInterrupt:
            client.close()
            s.close()
            print("Keyboard Interrupt. Exiting")
            sys.exit()

        except:
            print("In except")
            dir = "You tried to request a directory. At the moment, we are not supporting directory"
            print(dir)
            Error = 510
            print(Error)
            status = "404 Not Found"
            status2 = status.encode()
            header = a[2] + " " + status + "\n\n"
            headerB = header.encode()
            print(header)
            client.send(headerB)
            client.send(status2)
            # s.close()
        if Error == 0:
            print("EEE")
            print("type:" + type)
            file = a[1]
            print("file: " + file)
            status = "200 OK"
            Head_Cont(a, file, type, b, status)
            print("out of func.")


def PostData(request, pipe, Error):  # for POST request
    global times, Array
    last = len(request)
    add = request[last - 1]
    print(add)
    # default, can be made dyanamic by adding from Request List
    default = open("./document root directory/post.html", "rt")
    defi = default.read()
    #defin = defi.splitlines()
    # print(defin)
    index = defi.find("<HR>")
    out = defi[:index] + "<h1>Post Data</h1> <pre>" + \
        str(add) + "</pre>" + defi[index:]
    default.close()
    default = open("./document root directory/post.html", "wt")
    final = default.write(out)
    #default[i].append("<h1>Post Data</h1> <pre>", add, "</pre>")
    # print(default)
    default.close()
    defaultn = open("./document root directory/post.html", "rb")
    defsend = defaultn.read()
    print(defsend)
    size = os.stat("./document root directory/post.html")
    sizeS = size.st_size

    header = request[2] + " 200 OK" + "\n" + "Content-Type: " + \
        "text/html" + "\nContent-Length: " + \
        str(sizeS) + "\nConnection: " + pipe + "\n\n"
    headerB = header.encode()
    client.send(headerB)
    client.send(defsend)
    print("closing socket of POST")
    client.settimeout(None)
    client.close()


def main(client, address, Error):
    global times, Array, c
    print("Started Thread, name: " + str(c))
    start = time.time()
    # lock.acquire()
    while 1:
        print("just in main")
        try:
            data = client.recv(51200)
            x = 1
        except KeyboardInterrupt:
            client.close()
            s.close()
            print("Keyboard Interrupt. Exiting")
            sys.exit()
        except:
            print("No waiting client?????")
            print("closing socket")
            client.close()
            break
            x = 0

        print("client: " + str(client) + "address: " + str(address))
        a, b = address
        if int(b) <= 1024:
            print("Port numbers below 1024 have to be rejected.")
            sys.exit()

        num = client.fileno()
        print("File number:" + str(num))
        request = data.decode()
        print(request)
        if request:  # Only if request is not null
            request = request.split()
            print(request)
            times += 1
            if request[2] == "HTTP/1.1" or request[2] == "HTTP/1.0":

                # for line in request:
                #    if(line.startswith("Connection:")):
                #        line1 = line.split()
                #        Conn.append(line1[1])

                # client.send(data)

                print(request[5].lower())
                if request[5].lower() == "connection:":  # Persistence
                    if request[6].lower() == "keep-alive":
                        pipe = "keep-alive"
                        print(pipe)
                        keepalive = 1
                        print("In connection loop")
                        if request[0] != "POST":
                            print("setting timeout")
                            client.settimeout(float(Array[24]))
                    else:
                        pipe = "close"
                        print(pipe)
                        #start = time.time()
                        keepalive = 0
                else:
                    print("outside connection loop")
                    pipe = "close"

                # print(request2[0])
                # print(request)
                print("I am")
                # time.sleep(3)
                # print(request2[0])

                if request[0] == 'GET':
                    GetData(request, pipe, Error)
                elif request[0] == 'POST':
                    PostData(request, pipe, Error)
                    # break
                else:
                    header = request[2] + " " + "400 Bad Request"
                    headerB = header.encode()
                    status = "400 Bad Request"
                    status2 = status.encode()
                    client.send(headerB)
                    client.send(status2)
                print("Times: " + str(times))
                print("Enumerate:")
                print(threading.enumerate())

                # lock.release()
            else:
                file = "/400.html"
                type = "text/html"
                b = "close"
                status = "400 Bad Request"
                Head_Cont(a, file, type, b, status)
            if pipe == "close":
                print("closing socket")
                client.close()
                break
        else:
            break
    print("Ended Thread, name: " + str(c))
    end = time.time() - start
    print("Time taken for thread " + str(c) + " is " + str(end))

host = ""
try:
    DRoot = open("ws.conf.txt")
except:
    print("Configuration file not found.")
    sys.exit()
global Array, keepalive, c
#DR = DRoot.read()
Array = []
c = 0
i = 0
Error = 0

for line in DRoot:
    if(line.startswith("ListenPort")):
        line1 = line.split()
        Array.append(line1[1])  # port = Array[0]
    elif(line.startswith("DocumentRoot")):
        line1 = line.split()
        Array.append(line1[1])  # directory = Array[1]
    elif(line.startswith("DirectoryIndex")):
        line1 = line.split()
        # Array[2],[3],[4],[5] = default files
        Array.extend((line1[1], line1[2], line1[3], line1[4]))
    elif(line.startswith("ContentType")):
        line1 = line.split()
        # file type extension=Array[6], file type=Array[7], 8-9, 10-11, 12-13,
        # 14-15, 16-17, 18-19, 20-21, 22-23
        Array.extend((line1[1], line1[2]))
    elif(line.startswith("KeepaliveTime")):
        line1 = line.split()
        Array.append(line1[1])  # time in Array[24]
    else:
        x = 0


port = int(Array[0])
favi = ".ico"
Array.append(favi)  # ico in Array[25]
typef = "image/ico"
Array.append(typef)  # image/ico in Array[26]
print("Configuration file read as: \n")
print(Array)
if int(Array[0]) <= 1024:
    print(
        "Port numbers below 1024 are rejected. Pls change port number in configuration file")
    sys.exit()
#pipe = "keep-alive"

Conn = []
print("Awaiting Connection...")
times = 0
threads = []
keepalive = 1

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host, port))
    except socket.error as e:
        print(str(e))
    s.listen(400)
    input = [s]
    while 1:
        inputready, outputready, exceptready = select.select(input, [], [], 1)
        # print("started")
        for z in inputready:
            print("here")
            try:
                print("In outer loop")
                #client = "client" + str(i)
                client, address = s.accept()
                client.settimeout(None)  # for next instances
                #lock = threading.Lock()

                t = threading.Thread(
                    target=main, args=(client, address, Error))
                print("thread created")
                t.daemon = True
                t.start()
                t.join()
                i += 1
                c += 1
                # threads.append(t)
            except KeyboardInterrupt:
                s.close()
                print("Keyboard Interrupt. Exiting")
                sys.exit()
except KeyboardInterrupt:
    print("Keyboard Interrupt. Exiting")
    sys.exit()
except:
    status = "500 Internal Server Error: cannot allocate memory"
    type = "text/html"
    file = "/500.html"
    b = "close"
    a = "HTTP/1.1"
    Head_Cont(a, file, type, b, status)


# client.close()
"""
for POST, type the following on browser
data:text/html,<body onload="document.body.firstChild.submit()"><form method="post" action="http://localhost:9994/"><input value="hugh.mahn@person.com" name="email">
<input value="passwordsavedinhistory" name="password">

"""
quit()
