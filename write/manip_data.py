import csv
from models.movie import Movie


CSV_FILE = "data/movies.csv"


def add_movie():
    titre = input("Titre du film : ")
    annee_production = int(input("Année de sortie : "))
    genre = input("Genre : ")
    age_limite = int(input("Age limite : "))

    movie = Movie(titre, annee_production, genre, age_limite)

    # Écriture dans le CSV
    with open(CSV_FILE, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([movie.id, movie.titre, annee_production, genre, age_limite])

    print("Film ajouté avec succès !!!")

add_movie()

# Update le fichier CSV: 
def update_movie():
    movie_a_modifier = input("Titre de film à modifier : ")
    edit_data = []
    found = False
    
    with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
        lecteur = csv.DictReader(csvfile)
        for ligne in lecteur:
            edit_data.append(Movie(ligne['titre'], ligne['annee_production'], 
                                   ligne['genre'], ligne['age_limite']))
    
    for movie in edit_data:
        if movie.titre == movie_a_modifier:
            found = True
            nouveau_titre = input("Nouveau titre : ")
            nouvelle_annee = input("Nouvelle année : ")
            nouveau_genre = input("Nouveau genre : ")
            nouvel_age = input("Nouvel âge limite : ")
            
            movie.titre = nouveau_titre
            movie.annee_production = int(nouvelle_annee)
            movie.genre = nouveau_genre
            movie.age_limite = int(nouvel_age)
            break
    
    if not found:
        print("Film non trouvé.")
        return
    
    with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow(['id', 'titre', 'annee_production', 'genre', 'age_limite'])
        for movie in edit_data:
            writer.writerow([movie.id, movie.titre, movie.annee_production, 
                           movie.genre, movie.age_limite])
    
    print("Fichier CSV mis à jour.")

update_movie()

# # Delete film:

with open(CSV_FILE, 'r', encoding='utf-8') as csvfile:
    lecteur = csv.DictReader(csvfile)
    lignes = list(lecteur)
    Index = int(input("Entrer le Id de la ligne a supprimé : ")) - 1
if 0 <= Index  <= len(lignes):
        dell_data = lignes.pop(Index)
        print(f"ligne {Index +1} est supprimé .")
else:
        print("Index invalide") 

with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as fichier:
    if lignes:
        ecrivain = csv.DictWriter(fichier, fieldnames=lignes[0].keys())
        ecrivain.writeheader()
        ecrivain.writerows(lignes)
        print("Fichier CSV mis à jour.")
    else:
        print("Aucune donnée à écrire.")