# DasSpiel-Client-Python

Beispiel für Einbindung und Benutzung:

from flowerMeadow import FlowerMeadow

if __name__ == '__main__':
    # myGame = FlowerMeadow("192.168.33.1", 5555)
    myGame = FlowerMeadow.getInstance("192.168.33.1", 5555)
    #myGame.connect("Yannis")
    #myGame.spawnPlayer()
    #print(myGame.getStatus())
    #myGame.rotatePlayer(100)
    #myGame.movePlayer(20)
    
    # myGame.disconnect()
