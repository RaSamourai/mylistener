import socket
import SocketServer
from threading import Thread

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvaddr = ('localhost', 8800)
serversocket.bind(srvaddr)

class MyListener(Thread):

    def run(self):
        compteur = 0
        serversocket.listen(5)
        while True:
            print '\nEn attente de connexion :\n'
            connection, client_address = serversocket.accept()
            #accepter les connections provenant de l'exterieur
            compteur+=1
            list_connection.append(Connection(compteur,connection,client_address))
            #*****.append permet d'ajouter l'element a la fin de la liste
            print '\n\nNouvelle connexion etablie depuis :', list_connection[-1][1]

            printListConnection()
