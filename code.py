from socket import *
serverPort = 4321 #sets port
serverSocket = socket(AF_INET, SOCK_STREAM) #creates socket
#Prepare a sever socket
serverSocket.bind(('', serverPort))  #associates socket with this port
serverSocket.listen(1) #tells socket to listen for requests

while True:
    #Establish the connection
    print ('Listening on port %s ...' %serverPort)
    connectionSocket, addr = serverSocket.accept() #creates a socket specifically for this client
    print('Connection from: ' + str(addr)) #prints the address
	
    try:
        msg = connectionSocket.recv(1024) #receives message from client
        print('message = ' + str(msg))
        filename = msg.split()[1]
        print('filename = ' + str(filename))
        f = open(filename[1:]) #opens file and reads the contents
        output = f.read()
        print(output)
        connectionSocket.send(bytes('HTTP/1.1 200 OK \r\n\r\n'.encode()))  #sends a 200 OK header line
        connectionSocket.send(output.encode())  #send all of the data in the file
        print('200')
       
    except IOError:
        
       connectionSocket.send('HTTP/1.1 404 Not Found\n\n File Not found 404 '.encode('utf-8')) #sends an error message to be printed on the page
       print('404 error: File not found') 
    connectionSocket.close()  #closes the socket for this client
serverSocket.close() #closes the server socket
