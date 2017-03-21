import socket
import SocketServer
import sys
from threading import Thread
import time

myconnexionsocket=''
myclientaddr='0'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#creation du socket

srvaddr = ('localhost', 8800)

serversocket.bind(srvaddr)
#bind du socket sur un port et une @IP

print "Socket is starting up on %s port %s" % srvaddr

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

def sendMessage(self):
    contenu = raw_input("Ecrivez un message au client : ")
    if contenu == '':
        print "\nMessage vide, ecrivez ^^ !\n#FACEPALM\n"
    elif contenu == 'exit':
        print 'Closing socket'
        self.close()
    else:
        self.sendall(contenu)
        print "SENDED\n"
    pass

class mylistener(Thread):
    def run(self):
        compteur = 0
        serversocket.listen(5)
        while True:
            print 'En attente de connexion :\n'
            connection, client_address = serversocket.accept()
            #accepter les connections provenant de l'exterieur
            compteur+=1
            list_connection.append((connection, client_address, compteur))
            #*****.append permet d'ajouter l'element a la fin de la liste
            print '\n\nNouvelle connexion etablie depuis :', list_connection[-1][1]
            printListConnection()

class myTchatSend(Thread):
    def __init__(self, numcoS):
        Thread.__init__(self)
        self.numcoS = numcoS

    def run(self):
        #activeco = int(self.numcoS)
        #activeco -= 1
        self.numcoS -= 1
        mycurrentclient = list_connection[self.numcoS][0]
        myclientaddr = list_connection[self.numcoS][1][0]
        #serversocket.listen(5)
        #mycurrentclient, myclientaddr = serversocket.accept()
        print 'Connexion a :', list_connection[self.numcoS][1]
        while True:
            sendMessage(mycurrentclient)

class myTchatRecep(Thread):
    def __init__(self, numcoR):
        Thread.__init__(self)
        self.numcoR = numcoR

    def run(self):
        activeco = int(self.numcoR)
        activeco -= 1
        mycurrentwatch = list_connection[activeco][0]
        while True:
            data = mycurrentwatch.recv(255)
            #le 255 definit le nombre de caracteres envoye en une seule fois
            if data != '':
                if data == 'exit':
                    print "Connexion closed"
                    mycurrentwatch.close()
                    Thread_3.join()
                    break
                else:
                    #print '\nClient : "%s"' % data
                    print data
            continue

def selectConnexion(self):
    if self != '' and len(list_connection)!= 0:
        contenusC = int(self)
        if contenusC > 0 and contenusC <= len(list_connection):
                print "Connexion en cours..."
                print "..."
                Thread_2 = myTchatSend(contenusC)
                #time.sleep(0.01)
                Thread_3 = myTchatRecep(contenusC)
                print "..."
                Thread_2.start()
                Thread_3.start()
        else:
            printErrorMessage()
    else:
        printErrorMessage()
    Thread_2.join()
    pass

def testSelectCo(self):
    if len(list_connection) == 0:
        print "\nPAS DE CONNEXION POUR LE MOMENT !\n"
        return
    elif self.isdigit() == False and self !='':
        print "\nUn entier boloss ^^\n"
    elif self == '' and len(list_connection) >= 1:
        printErrorMessage()
    elif int(self) > len(list_connection):
        print "\nHORS PLAGE ! ! !\n"
    else:
        return 'OK'
    pass

Thread_1 = mylistener()
Thread_1.start()
time.sleep(0.01)
myTchatSend
while True:
    contenu = raw_input("Saisir le numero de la connexion sur laquelle se connecter : ")
    result = testSelectCo(contenu)
    if result == 'OK':
        selectConnexion(contenu)

Thread_1.join()
#Thread_2.join()
#Thread_3.join()
