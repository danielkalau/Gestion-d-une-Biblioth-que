def ajouter_utilisateur(bibliotheque, id, nom, email):
    # Créer un dictionnaire représentant le nouvel utilisateur
    nouvel_utilisateur = {
        'id': id,
        'nom': nom,
        'email': email
    }
    
    # Ajouter le nouvel utilisateur à la liste des utilisateurs de la bibliothèque
    bibliotheque['utilisateurs'].append(nouvel_utilisateur)
