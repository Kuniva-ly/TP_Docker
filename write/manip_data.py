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
 
