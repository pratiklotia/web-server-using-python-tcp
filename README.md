# web-server-using-python-tcp
A web-server program for reliable data transfer and handle requests from client.

Author: Pratik Lotia

Python programs executable in v3.1 and higher versions (done on v3.4)


Usage (on Command Prompt): webServer.py

Default Port number set in configuration file: 9994 (check configuration file)
Note:
1. test file - (testclient.py) for Performance Evaluation included. It contains sleep function (commented) to check
whether timeout (persistence of connection) happens on server properly.
2. Pipelining supported (keep-alive)
3. Currently supports HTTP - GET and POST* only
4. For checking HTTP POST request:
simply in your browser, enter: (please remove the extra quotation marks (") from both the sides of "<" and ">".

data:text/html, "<"body onload="document.body.firstChild.submit()"">""<"form method="post" action="http://localhost:9994/"">""<"input value="hugh.mahn@person.com" name="email"">"
"<"input value="passwordsavedinhistory" name="password"">"



The text in 'value' and 'name' can be edit. By this way, server receives POST request. By default, it will edit a 
file called 'post.html' (included) and show the data. For simplicity, data is not decrypted, hence you might see text including '&' and other variables.
If you change the port number in Config file, pls also change it in the POST request.

4. Pipelining done. Can be checked by performance evaluation and checking data on server side.

All the contents of document root directory have been attached. Please make a directory named as 'document root directory'
 and paste all the contents as it appears in the directory here.
The name of the diretory, if changed - should be changed in the program too.


Default file: /index.html

The file 'index2.html' contains example of support for all file types.

You can edit the configuration file to change 'timeout' time and can add support for more file types.

PortNumber>1024 to be used.

Failure to enter proper port number will result in error
and program will exit.

Error handling is done properly
Keyboard Interrupt also handled

Functional process:
Server reads configuration files and stores it in a list
Listens & Accepts request from client (Syn, Syn-Ack (on client side), Ack)
Creates Instance of Thread
(Keyboard Interrupt handled if occurs)
Thread function spawns a thread to carry out the process and server is again ready to accept more requests.
Thread calls main function to print addresses, check version of HTTP, decide persistency and finally checks type
of request. For GET, it calls GetData and for POST, it uses PostData.
GetData:
It will first check if default files is asked else will check whether file type supported. It will handle errors for
file type not supported and invalid URL.
It will call Head_Cont function to send header and data respectively

PostData:
Will open /post.html file by default to edit it. This can be changed and assigned dynamically.
Post edits the html file with the data obtained in request and calls Head_Cont function to send header and data.
