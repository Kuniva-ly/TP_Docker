import csv
from typing import List, Dict, Optional

DATA_FILE ="data/movies.csv"

def field(row: Dict[str, str], *aliases: str) -> str:
    for k in aliases:
        if k in row and row[k] is not None:
            return str(row[k]).strip()
    return ""

def read_movies() -> List[Dict[str, str]]:
    with open(DATA_FILE, mode="r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def get_movie_by_title(title: str) -> Optional[Dict[str, str]]:
    t = title.strip().lower()
    for m in read_movies():
        if field(m, "title", "titre").lower() == t:
            return m
    return None

def get_movies_by_age_limit(max_age: int) -> List[Dict[str, str]]:
    res = []
    for m in read_movies():
        try:
            age = int(field(m, "age_limit", "age_limite"))
            if age <= max_age:
                res.append(m)
        except ValueError:
            pass
    return res

def get_movies_by_genre(genre: str) -> List[Dict[str, str]]:
    g = genre.strip().lower()
    return [m for m in read_movies() if field(m, "genre").lower() == g]

def get_movies_by_year_range(start_year: int, end_year: int) -> List[Dict[str, str]]:
    if start_year > end_year:
        start_year, end_year = end_year, start_year
    res = []
    for m in read_movies():
        try:
            y = int(field(m, "year", "annee_production"))
            if start_year <= y <= end_year:
                res.append(m)
        except ValueError:
            pass
    return res

def print_list(movies: List[Dict[str, str]]) -> None:
    if not movies:
        print("Aucun résultat.")
        return
    for m in movies:
        print(f"- {field(m,'title','titre')} | {field(m,'genre')} | "
              f"{field(m,'year','annee_production')} | âge < {field(m,'age_limit','age_limite')}")

if __name__ == "__main__":
    while True:
        print("\n=== MENU ===")
        print("1) Film par titre")
        print("2) Films par limite d'âge")
        print("3) Films par genre")
        print("4) Films entre deux années")
        print("5) Quitter")
        choice = input("Choix: ").strip()

        try:
            if choice == "1":
                t = input("Titre: ")
                m = get_movie_by_title(t)
                if m:
                    print(f"{field(m,'title','titre')} | {field(m,'genre')} | "
                          f"{field(m,'year','annee_production')} | âge < {field(m,'age_limit','age_limite')}")
                else:
                    print("Aucun film avec ce titre.")
            elif choice == "2":
                a = int(input("Âge maximum: "))
                print_list(get_movies_by_age_limit(a))
            elif choice == "3":
                g = input("Genre: ")
                print_list(get_movies_by_genre(g))
            elif choice == "4":
                s = int(input("Année début: "))
                e = int(input("Année fin: "))
                print_list(get_movies_by_year_range(s, e))
            elif choice == "5":
                break
            else:
                print("Choix invalide.")
        except FileNotFoundError:
            print(f"Fichier CSV introuvable: {DATA_FILE}")
        except Exception as ex:
            print(f"Erreur: {ex}")
