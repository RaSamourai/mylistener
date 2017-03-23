
#str = "123456";  # Only digit in this string
#print str.isdigit()

#str = "this is string example....wow!!!";
#print str.isdigit()

class Personne:

    def __init__(self, pNom, pPrenom, pAge):
        self.nom=pNom
        self.prenom=pPrenom
        self.age=pAge

    def light(self):
        print "LIGHT !"

personne = Personne("tavares", "alex", "24")
print personne.nom
print personne.prenom
print personne.age

personne.nom = "Pannier"
print personne.nom
print personne.prenom
print personne.age

personne.light()


serversocket.bind((socket.gethostname(), 80))
#become a server socket
serversocket.listen(5)
#A couple things to notice: we used socket.gethostname()
#so that the socket would be visible to the outside world.
#If we had used s.bind(('localhost', 80)) or s.bind(('127.0.0.1', 80))
#we would still have a “server” socket, but one that was
#only visible within the same machine. s.bind(('', 80))
#specifies that the socket is reachable by any address the machine happens to have.
