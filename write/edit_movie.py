import csv;

edit_data = []
CSV_File = "data/movies.csv"
with open(CSV_File, 'r', encoding='utf-8') as csvfile:
    lecteur = csv.DictReader(csvfile)
    for ligne in lecteur:
        if ligne['titre'] == 'Film Ancien':
            ligne['titre'] = 'Film Corrigé'
        edit_data.append(ligne)

with open(CSV_File, mode='w', encoding='utf-8', newline='') as fichier:
    if edit_data:
        ecrivain = csv.DictWriter(fichier, fieldnames=edit_data[0].keys())
        ecrivain.writeheader()
        ecrivain.writerows(edit_data)

print("Fichier CSV mis à jour.")
# csvfile = open("data/movies.csv")
# myreader = csv.reader(csvfile)
# for row in myreader:
#     print(row)
