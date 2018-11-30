#! python3

import socket

class DasSpielV1:
    '''This class handles the socket communication to the server'''
    ip = "" 
    port = 0
    distToWall = 0.0

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def sendMessage(self, msg):
        client_socket = socket.socket()  # instantiate
        client_socket.settimeout(3000)
        client_socket.connect((self.ip, self.port))  # connect to the server
        client_socket.send(msg.encode())  # send message
        if "STATUS;" in msg or "DIST;" in msg:
            while True:
                rcvMsg = client_socket.recv(1024).decode()  # receive response
                print('Received from server: ' + rcvMsg)  # show in terminal
                if ";" in rcvMsg:
                    break
        client_socket.close()  # close the connection
		
    def connect(self, username):
        self.sendMessage("CONNECT|" + username + ";")	

    def disconnect(self):
        self.sendMessage("DISCONNECT;")
	
    def spawnPlayer(self):
        self.sendMessage("SPAWN;")
	
    def deletePlayer(self):
        self.sendMessage("DELETE;")		

    def rotatePlayer(self, angle):
        self.sendMessage("ROTATE|{0};".format(angle))

    def movePlayer(self, speed):
        self.sendMessage("MOVE|{0};".format(speed))
	
    def shootBullet(self):
        self.sendMessage("SHOOT;")
	    
    def startDrawing(self, color):
        self.sendMessage("DRAW|" + color + ";")
	
    def stopAndClearDrawing(self): 
        self.sendMessage("STOP_DRAWING;")
	
    def getStatus(self):
        self.sendMessage("STATUS;")
		
    def getDistToWall(self):
        self.sendMessage("DIST;")
        return self.distToWall        
		
	def getPlayersInRadius(self, radius) 
		self.sendMessage("SURROUNDINGS|" + radius + ";")
	

