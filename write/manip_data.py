import csv
from models.movie import Movie
from exceptions import InvalidAgeLimitException, InvalidGenreException, InvalidTitleException, InvalidYearException

CSV_FILE = "data/movies.csv"


# Ajouter un film

def add_movie():
    try:
        titre = input("Titre du film : ")
        if not titre.strip():
            raise InvalidTitleException("Le titre ne peut pas être vide.")
        
        annee_production = int(input("Année de sortie : "))
        if annee_production < 1800 or annee_production > 2026:
            raise InvalidYearException("Année invalide.")

        genre = input("Genre : ")
        if not genre.strip():
            raise InvalidGenreException("Le genre ne peut pas être vide.")

        age_limite = int(input("Age limite : "))
        if age_limite < 0:
            raise InvalidAgeLimitException("L'âge limite doit être positif.")

        movie = Movie(titre, annee_production, genre, age_limite)

        with open(CSV_FILE, "a", newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([movie.id, movie.titre, movie.annee_production, movie.genre, movie.age_limite])

        print("Film ajouté avec succès !!!")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide pour l'année ou l'âge limite.")
    except (InvalidTitleException, InvalidYearException, InvalidGenreException, InvalidAgeLimitException) as e:
        print(f"Erreur : {e}")


# Mettre à jour un film

def update_movie():
    try:
        movie_a_modifier = input("Titre du film à modifier : ")
        edit_data = []
        found = False

        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            lecteur = csv.DictReader(csvfile)
            for ligne in lecteur:
                edit_data.append(Movie(ligne['titre'], int(ligne['annee_production']), 
                                       ligne['genre'], int(ligne['age_limite'])))

        for movie in edit_data:
            if movie.titre == movie_a_modifier:
                found = True

                nouveau_titre = input("Nouveau titre : ")
                if not nouveau_titre.strip():
                    raise InvalidTitleException("Le titre ne peut pas être vide.")

                nouvelle_annee = int(input("Nouvelle année : "))
                if nouvelle_annee < 1800 or nouvelle_annee > 2100:
                    raise InvalidYearException("Année invalide.")

                nouveau_genre = input("Nouveau genre : ")
                if not nouveau_genre.strip():
                    raise InvalidGenreException("Le genre ne peut pas être vide.")

                nouvel_age = int(input("Nouvel âge limite : "))
                if nouvel_age < 0:
                    raise InvalidAgeLimitException("L'âge limite doit être positif.")

                movie.titre = nouveau_titre
                movie.annee_production = nouvelle_annee
                movie.genre = nouveau_genre
                movie.age_limite = nouvel_age
                break

        if not found:
            print("Film non trouvé.")
            return

        with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as fichier:
            writer = csv.writer(fichier)
            writer.writerow(['id', 'titre', 'annee_production', 'genre', 'age_limite'])
            for movie in edit_data:
                writer.writerow([movie.id, movie.titre, movie.annee_production, movie.genre, movie.age_limite])

        print("Fichier CSV mis à jour.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide pour l'année ou l'âge limite.")
    except (InvalidTitleException, InvalidYearException, InvalidGenreException, InvalidAgeLimitException) as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


# Supprimer un film

def delete_movie():
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
            lecteur = csv.DictReader(csvfile)
            lignes = list(lecteur)

        Index = int(input("Entrer le Id de la ligne à supprimer : ")) - 1

        if 0 <= Index < len(lignes):
            dell_data = lignes.pop(Index)
            print(f"Ligne {Index + 1} supprimée : {dell_data}")
        else:
            print("Index invalide")
            return

        with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as fichier:
            if lignes:
                ecrivain = csv.DictWriter(fichier, fieldnames=lignes[0].keys())
                ecrivain.writeheader()
                ecrivain.writerows(lignes)
                print("Fichier CSV mis à jour.")
            else:
                print("Aucune donnée à écrire.")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide pour l'ID.")
    except FileNotFoundError:
        print("Erreur : Fichier CSV non trouvé.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

add_movie()
update_movie()
delete_movie()
