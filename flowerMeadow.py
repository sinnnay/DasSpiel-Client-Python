#! python3

import socket

class FlowerMeadow:
    '''This class handles the socket communication to the server'''
    ip = "" 
    port = 0
    distToWall = 0.0 or None
    messageFromServer = "" or None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def sendMessage(self, msg):
        try:
            client_socket = socket.socket()  # instantiate
            client_socket.connect((self.ip, self.port))  # connect to the server
            client_socket.send(msg.encode())  # send message
            client_socket.settimeout(3)
            if "STATUS;" in msg or "DIST;" in msg or "SURR_PLAYERS" in msg or "SURR_PICKUPS" in msg or "DIR_VECTOR;" in msg or "CONNECT" in msg:
                while True:
                    rcvMsg = client_socket.recv(1024).decode()  # receive response
                    if ";" in rcvMsg:
                        break
                if "DIST;" in msg:
                    self.distToWall = rcvMsg
                if "CONNECT" in msg:
                    print(rcvMsg)  
                else:
                    self.messageFromServer = rcvMsg
            client_socket.close()
        except socket.timeout:
            print("Server antwortet nicht")
        except socket.error:
            print("Verbindung fehlgeschlagen! Bitte überprüfe deine Eingaben für IP-Adresse und Portnummer. Der Server läuft vielleicht noch nicht.")
        finally:
            client_socket.close()
		
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
	
    def shoot(self):
        self.sendMessage("SHOOT;")
	    
    def startDrawing(self, color):
        self.sendMessage("DRAW|" + color + ";")
	
    def stopAndClearDrawing(self): 
        self.sendMessage("STOP_DRAWING;")
	
    def startMowing(self): 
        self.sendMessage("MOW;")

    def stopMowing(self): 
        self.sendMessage("STOP_MOWING;")

    def getStatus(self):
        self.sendMessage("STATUS;")
        return self.messageFromServer

    def getDistToWall(self):
        self.sendMessage("DIST;")
        return self.distToWall

    def getPlayersInRadius(self, radius):
        self.sendMessage("SURR_PLAYERS|" + radius + ";")
        return self.messageFromServer

    def getPickUpsInRadius(self, radius):
        self.sendMessage("SURR_PICKUPS|" + radius + ";")
        return self.messageFromServer

    def getDirectionVector(self):
        self.sendMessage("DIR_VECTOR;")
        return self.messageFromServer

