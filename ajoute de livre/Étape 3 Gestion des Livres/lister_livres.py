def lister_livres(bibliotheque):
    # Vérifier s'il y a des livres dans la bibliothèque
    if not bibliotheque['livres']:
        return "Aucun livre disponible dans la bibliothèque."
    
    # Construire une chaîne de caractères pour afficher la liste des livres
    liste_des_livres = "Liste des livres dans la bibliothèque:\n"
    for livre in bibliotheque['livres']:
        liste_des_livres += f"ID: {livre['id']}, Titre: {livre['Titre']}, Auteur: {livre['Auteur']}, Genre: {livre['Genre']}, Disponible: {'Oui' if livre['Disponible'] else 'Non'}\n"
    
    return liste_des_livres

# Exemple d'utilisation
bibliotheque = {
    'livres': [
        {'id': 1, 'Titre': 'Le Petit Prince', 'Auteur': 'Antoine de Saint-Exupéry', 'Genre': 'Fiction', 'Disponible': True},
        {'id': 2, 'Titre': '1984', 'Auteur': 'George Orwell', 'Genre': 'Dystopie', 'Disponible': False}
    ]
}

print(lister_livres(bibliotheque))
