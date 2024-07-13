def supprimer_livre_ui():
    # Obtenir le titre du livre à partir du champ de saisie
    titre = entry_titre.get()
    
    # Appeler la fonction pour supprimer définitivement le livre
    result = supprimer_livre_definitivement(titre)
    
    # Afficher un message d'information avec le résultat de la suppression
    messagebox.showinfo("Résultat", result)
    
    # Enregistrer la transaction de suppression
    enregistrer_transaction("Supprimer", titre)
    
    # Mettre à jour l'affichage des livres dans l'interface utilisateur
    afficher_livres_ui()
    
    # Réinitialiser les champs de saisie de l'interface utilisateur
    reset_fields()
