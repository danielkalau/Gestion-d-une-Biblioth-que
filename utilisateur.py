class Utilisateur:
    def __init__(self, id_utilisateur, nom, email):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Utilisateur[id={self.id_utilisateur}, nom={self.nom}, email={self.email}]"
