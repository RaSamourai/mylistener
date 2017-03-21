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
        print "Contenu vide, ecrivez ^^ ! \n#FACEPALM\n"
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
                    print 'Recu : "%s"' % data
                    #p = Popen([data], stdin=PIPE, stdout=PIPE, bufsize=1)
                    #print p.stdout.readline(), # read the first line
                    #for i in range(10):
                        #print >>p.stdin, i
                        #p.stdin.flush()
                        #print p.stdout.readline(),
                    result = []
                    p = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE)
                    #q = Popen(data, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
                    #print p.stdout
                    for line in p.stdout:
                        #line = line.rstrip()

                        if line != '':
                            print line,
                            #la , en fin de ligne permet d'empecher le retour chariot
                            clientsocket.sendall(line,)
                            #clientsocket.sendall("EMPTY\n")
                            #print "EMPTY"
                        #else:
                            #clientsocket.sendall(line)
                            #result.append(line)
                            #print line
                    #print result
                    #print p.stdout
                    #clientsocket.sendall(''.join([line for line in p.stdout.xreadlines()]))
                    #output = p.stdout
                    #clientsocket.sendall(output)
                    #print output
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
