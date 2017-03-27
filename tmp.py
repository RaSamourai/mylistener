import socket
import SocketServer
import sys
from threading import Thread
import time
from connection import Connection
from listener import MyListener

###########################################################################################################################################
class MyTchatRecep(Thread):

    def __init__(self, numcoR):
        Thread.__init__(self)
        self.numcoR = numcoR
        self.mycurrentconnection = list_connection[numcoR-1]

    def run(self):
        activeco = int(self.numcoR)
        activeco -= 1
        while True:
            data = self.mycurrentconnection.connection.recv(255)
            #le 255 definit le nombre de caracteres envoye en une seule fois
            if data != '':
                if data == 'exit':
                    print "Connexion closed"
                    self.mycurrentconnection.connection.close()
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
        self.mycurrentclient = list_connection[numcoS-1]
        self.myclientaddr = list_connection[numcoS-1][1][0]

    def run(self):
        activeco = int(self.numcoS)
        activeco -= 1
        #serversocket.listen(5)
        #mycurrentclient, myclientaddr = serversocket.accept()
        print activeco
        print 'Connexion a :', list_connection[activeco][1]
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
        thread_2.mycurrentclient.connection.close()
        thread_3.mycurrentwatch.connection.close()
        return False
    else:
        self.sendall(contenu)
        print "SENDED\n"
        return True
    pass
###########################################################################################################################################
myconnexionsocket=''
myclientaddr='0'
print "Socket is starting up on localhost port 8800"
list_connection = []
thread_1 = MyListener()
thread_1.start()

while True:
    ok0=False
    while ok0 != True:
        numCoString = raw_input("Saisir le numero de la connexion sur laquelle se connecter : ")
        ok0 = TestSelectCo(numCoString)
        print ok0
        if ok0 == True:
            numCoString = int(numCoString)
            thread_2 = MyTchatSend(numCoString)
            thread_2.start()
            thread_3 = MyTchatRecep(numCoString)
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
