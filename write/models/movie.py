class Movie:
    id_compteur = 31

    def __init__(self,titre:str, annee_production:int, genre:str, age_limite:int):
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite
        self.id = Movie.id_compteur
        Movie.id_compteur += 1

    def __str__(self):
            return f"ID: {self.id}, Titre: {self.titre}, Année: {self.annee_production}, Genre: {self.genre}, Âge limite: {self.age_limite}"
