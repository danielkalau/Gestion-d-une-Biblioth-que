import json
from datetime import datetime

# Classe pour représenter un Livre
class Livre:
    def __init__(self, id_livre, titre, auteur):
        self.id_livre = id_livre
        self.titre = titre
        self.auteur = auteur
        self.disponible = True
        self.emprunte_par = None
        self.date_emprunt = None

# Classe pour représenter un Utilisateur
class Utilisateur:
    def __init__(self, id_utilisateur, nom):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.livres_empruntes = []

# Fonction pour permettre l'emprunt d'un livre
def emprunter_livre(utilisateur, livre):
    if livre.disponible:
        livre.disponible = False
        livre.emprunte_par = utilisateur.id_utilisateur
        livre.date_emprunt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        utilisateur.livres_empruntes.append(livre.id_livre)
        print(f"Livre '{livre.titre}' emprunté par {utilisateur.nom}.")
    else:
        print(f"Le livre '{livre.titre}' n'est pas disponible.")

# Fonction pour permettre le retour d'un livre emprunté
def retourner_livre(utilisateur, livre):
    if livre.id_livre in utilisateur.livres_empruntes:
        livre.disponible = True
        livre.emprunte_par = None
        livre.date_emprunt = None
        utilisateur.livres_empruntes.remove(livre.id_livre)
        print(f"Livre '{livre.titre}' retourné par {utilisateur.nom}.")
    else:
        print(f"L'utilisateur {utilisateur.nom} n'a pas emprunté le livre '{livre.titre}'.")

# Fonction pour sauvegarder les données dans des fichiers JSON
def sauvegarder_donnees(livres, utilisateurs, fichier_livres, fichier_utilisateurs):
    livres_data = [{'id_livre': livre.id_livre, 'titre': livre.titre, 'auteur': livre.auteur, 
                    'disponible': livre.disponible, 'emprunte_par': livre.emprunte_par, 
                    'date_emprunt': livre.date_emprunt} for livre in livres]
    utilisateurs_data = [{'id_utilisateur': utilisateur.id_utilisateur, 'nom': utilisateur.nom, 
                          'livres_empruntes': utilisateur.livres_empruntes} for utilisateur in utilisateurs]
    
    with open(fichier_livres, 'w') as f_livres:
        json.dump(livres_data, f_livres, indent=4)
        
    with open(fichier_utilisateurs, 'w') as f_utilisateurs:
        json.dump(utilisateurs_data, f_utilisateurs, indent=4)
        
    print("Données sauvegardées avec succès.")

# Exemple d'utilisation
livre1 = Livre(1, "1984", "George Orwell")
livre2 = Livre(2, "Le Petit Prince", "Antoine de Saint-Exupéry")
utilisateur1 = Utilisateur(1, "Alice")

emprunter_livre(utilisateur1, livre1)
retourner_livre(utilisateur1, livre1)

livres = [livre1, livre2]
utilisateurs = [utilisateur1]
sauvegarder_donnees(livres, utilisateurs, 'livres.json', 'utilisateurs.json')
