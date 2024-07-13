def ajouter_livre(titreLivre, auteur, genreLivre):
    livres = charger_livres()
    
    if not (valider_titre(titreLivre) and valider_genre(genreLivre) and valider_auteur(auteur)):
        return "Les informations fournies ne sont pas valides."

    if verifier_doublon_titre(livres, titreLivre):
        return "Un livre avec ce titre existe déjà."
    
    idLivre = nouveau_id(livres)
    livre = {
        "id": idLivre,
        "Titre": titreLivre,
        "Auteur": auteur,
        "Genre": genreLivre,
        "Disponible": True
    }
    
    livres.append(livre)
    sauvegarder_livres(livres)
    
    return "Les nouvelles données ont été ajoutées à donnees.json"
