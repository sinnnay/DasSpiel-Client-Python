# DasSpiel-Client-Python

Beispiel für Einbindung und Benutzung:

from dasSpiel import DasSpielV1

if __name__ == '__main__':
    myGame = DasSpielV1("192.168.33.1", 53697)
    myGame.connect("Yannis")
    myGame.spawnPlayer()
    myGame.movePlayer(50)
    # myGame.disconnect()
