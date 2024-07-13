def supprimer_utilisateur(bibliotheque, id):
    # Filtrer la liste des utilisateurs pour exclure celui avec l'identifiant donné
    bibliotheque['utilisateurs'] = [
        utilisateur for utilisateur in bibliotheque['utilisateurs'] 
        if utilisateur['id'] != id
    ]
