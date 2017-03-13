import socket
import sys
import time


srvaddr = ('localhost', 8800)
contenu = ''
#parametre de connexion au srv pour le client

print 'Connecting to %s port %s' % srvaddr
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(srvaddr)

while True:
    socket.sendall(u"Hey my name is Olivier!")
    #data = clientsocket.recv(255)
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

clientsocket.close()
print 'Closing socket'
