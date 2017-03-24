class Connection(object):
    ident = ""
    connection = None
    adresse = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, ident, connection, adresse):
        self.ident = ident
        self.connection = connection
        self.adresse = adresse
