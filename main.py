from livre import Livre
from utilisateur import Utilisateur
from bibliotheque import Bibliotheque

def main():
    # Initialisation de la bibliothèque
    biblio = Bibliotheque()

    # Création de quelques livres
    livre1 = Livre(1, "1984", "George Orwell", "Dystopie")
    livre2 = Livre(2, "Le Petit Prince", "Antoine de Saint-Exupéry", "Conte")

    # Création de quelques utilisateurs
    utilisateur1 = Utilisateur(1, "Alice", "alice@example.com")
    utilisateur2 = Utilisateur(2, "Bob", "bob@example.com")

    # Ajout des livres et des utilisateurs à la bibliothèque
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_utilisateur(utilisateur1)
    biblio.ajouter_utilisateur(utilisateur2)

    # Affichage des livres et des utilisateurs
    print("Livres dans la bibliothèque:")
    biblio.afficher_livres()

    print("\nUtilisateurs de la bibliothèque:")
    biblio.afficher_utilisateurs()

if __name__ == "__main__":
    main()
