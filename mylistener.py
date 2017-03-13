#importation de la librairie socket
import socket
import SocketServer
import sys
from threading import Thread
import time

myconnexionsocket=''
myclientaddr='0'

#create a socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host, and a well-known port
srvaddr = ('localhost', 8800)
serversocket.bind(srvaddr)
print "Socket is starting up on %s port %s" % srvaddr
#become a server socket

list_connection = []


def printListConnection():
    print "\n######################"
    print "Liste des connexions :"

    for i in range (0,len(list_connection)):
        print list_connection[i][1], " num :", i+1

    print "Nombre de connexion total :",len(list_connection)
    print "######################\n"
    pass

def printErrorMessage():
    printListConnection()
    print "Merci de formuler un choix FDP ^^ !\n"
    pass

def sendMessage():
    print "Ecrivez un message : "
    contenu = raw_input()

    if contenu == '':
        print "ECRIVEZ, ECRIRE ! ECRIRE ! (facepalm)"
    else:
        mycurrentclient.sendall("bite")
        print "message envoyer, en attentes de reponses"
    pass


class mylistener(Thread):

    def run(self):
        compteur = 0
        serversocket.listen(5)
        while True:
            print 'En attente de connexion :\n'
            #accept connections from outside
            connection, client_address = serversocket.accept()
            compteur+=1

            list_connection.append((connection, client_address, compteur))
            #*****.append permet d'ajouter l'element a la fin de la liste
            print 'Nouvelle connexion etablie depuis :', list_connection[-1][1]

            #print compteur
            printListConnection()
            #myclientaddr = client_address
            # Receive the data in small chunks and retransmit it
            #break

class mytchat(Thread):

    def __init__(self, numco):
        Thread.__init__(self)
        self.numco = numco

    def run(self):

        activeco = int(self.numco)

        print activeco
        activeco -= 1

        print activeco

        #activeco = int(activeco)
        #on met le int ici pour obliger activeco a prendre le type int pour entier, avec les donnees de self numco
        #print activeco
        print 'Connexion a :', list_connection[activeco][1]
        print "Wait for SMS"
        while True:
            #if len(list_connection) == 0:
                 #time.sleep(1)
                 #continue
                 #remplace un else et renvoie au debut du while
            #data = connection.recv(255)
            #lock.acquire()
            mycurrentclient = list_connection[activeco][0]
            #mycurrentclient = list_connection[-1][0]
            myclientaddr = list_connection[activeco][1][0]

            serversocket.listen(5)
            mycurrentclient, myclientaddr = serversocket.accept()
            data = mycurrentclient.recv(255)

            print data

            #le 255 definit le nombre de caracteres envoye en une seule fois
            if data != '':
                print 'Recu "%s"' % data

            contenu = raw_input("Saisir le texte a afficher sur le SRV : \nexit si vous voulez quitter\n" )

            if contenu != '':
                if contenu == 'exit':
                    print 'Closing socket'
                    clientsocket.close()
                    break
                else:
                    clientsocket.sendall(contenu)
                continue

Thread_1 = mylistener()
Thread_1.start()

while True:

    contenu = raw_input("Saisir le numero de la connexion sur laquelle se connecter : ")

    if contenu != '' and len(list_connection)!=0:
        contenu = int(contenu)
        if contenu > 0 and contenu <= len(list_connection):
                contenu = int(contenu)
                print "Connexion en cours..."
                print "..."
                Thread_2 = mytchat(contenu)
                print "..."
                Thread_2.start()
                break
        else:
            printErrorMessage()
    else:
        printErrorMessage()
    continue


Thread_1.join()
Thread_2.join()






        # Clean up the connection
        #connection.close()
