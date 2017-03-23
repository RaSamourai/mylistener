import socket
import SocketServer
import sys
from threading import Thread
import time
###########################################################################################################################################
class MyListener(Thread):

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

class MyTchatRecep(Thread):

    def __init__(self, numcoR):
        Thread.__init__(self)
        self.numcoR = numcoR
        self.mycurrentwatch = list_connection[numcoR-1][0]

    def run(self):
        activeco = int(self.numcoR)
        activeco -= 1
        while True:
            data = self.mycurrentwatch.recv(255)
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

class MyTchatSend(Thread):

    def __init__(self, numcoS):
        Thread.__init__(self)
        self.numcoS = numcoS
        self.mycurrentclient = list_connection[numcoS-1][0]
        self.myclientaddr = list_connection[numcoS-1][1][0]

    def run(self):
        activeco = int(self.numcoS)
        activeco -= 1

        #serversocket.listen(5)
        #mycurrentclient, myclientaddr = serversocket.accept()
        print activeco
        print 'Connexion a :', list_connection[activeco][1]
        #contenu = raw_input("Ecrivez un message au client : ")
        #if contenu == 'exit':
            #print 'Closing socket'
            #thread_2.mycurrentclient.close()
            #thread_3.mycurrentwatch.close()
        #else:
            #self.mycurrentclient.sendall(contenu)
            #print "SENDED\n"
###########################################################################################################################################
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

def TestSelectCo(self):
    if len(list_connection) == 0:
        print "\nPAS DE CONNEXION POUR LE MOMENT !\n"
        return
    elif self == '' and len(list_connection) >= 1:
        printErrorMessage()
    elif self.isdigit() == False and self !='':
        print "\nUn entier boloss ^^\n"
    elif int(self) > len(list_connection) or int(self) == 0:
        print "\nHORS PLAGE ! ! !\n"
    else:
        return True
    pass

def SendMessage(self):
    contenu = raw_input("Entrer CMD : ")
    if contenu == '':
        print "\nMessage vide, ecrivez ^^ !\n#FACEPALM\n"
        return True
    elif contenu == 'exit':
        print 'Closing socket'
        thread_2.mycurrentclient.close()
        thread_3.mycurrentwatch.close()
        return False
    else:
        self.sendall(contenu)
        print "SENDED\n"
        return True
    pass
###########################################################################################################################################
myconnexionsocket=''
myclientaddr='0'
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvaddr = ('localhost', 8800)
serversocket.bind(srvaddr)
print "Socket is starting up on %s port %s" % srvaddr
list_connection = []
thread_1 = MyListener()
thread_1.start()

while True:
    ok0=False
    while ok0 != True:
        contenu = raw_input("Saisir le numero de la connexion sur laquelle se connecter : ")
        ok0 = TestSelectCo(contenu)
        print ok0
        if ok0 == True:
            contenu = int(contenu)
            thread_2 = MyTchatSend(contenu)
            thread_2.start()
            thread_3 = MyTchatRecep(contenu)
            thread_3.start()
        else:
            continue

    ok1=True
    while ok1 == True:
        ok1 = SendMessage(thread_2.mycurrentclient)

        continue

    #ok=sendMessage(thread_2.mycurrentclient)
    #print ok
    #if ok == False:
        #print "LOOP HAS ENDED ! ! !"
        #print ok
#sendMessage(thread_2.mycurrentclient)