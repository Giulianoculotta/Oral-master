import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

""" Liste des films"""
films = [
    ["Le Seigneur des Anneaux : Le Retour du Roi", "fantastique", "Elijah Wood", 2003],
    ["Le Parrain", "drame", "Marlon Brando", 1972],
    ["Inception", "science-fiction", "Leonardo DiCaprio", 2010],
    ["Star Wars : Episode IV - Un nouvel espoir", "science-fiction", "Mark Hamill", 1977],
    ["La Liste de Schindler", "drame", "Liam Neeson", 1993],
    ["Le Silence des Agneaux", "thriller", "Jodie Foster", 1991],
    ["Retour vers le futur", "science-fiction", "Michael J. Fox", 1985],
    ["Fight Club", "drame", "Brad Pitt", 1999],
    ["Forrest Gump", "drame", "Tom Hanks", 1994],
    ["Le Roi Lion", "animation", "Matthew Broderick", 1994],
    ["Avatar", "science-fiction", "Sam Worthington", 2009],
    ["The Lord of the Rings: The Fellowship of the Ring", "fantasy", "Elijah Wood", 2001],
    ["The Godfather: Part II", "crime", "Al Pacino", 1974],
    ["The Dark Knight Rises", "action", "Christian Bale", 2012],
    ["The Shawshank Redemption", "drama", "Tim Robbins", 1994],
    ["Inglourious Basterds", "war", "Brad Pitt", 2009],
    ["The Matrix", "action", "Keanu Reeves", 1999],
    ["Schindler's List", "biography", "Liam Neeson", 1993],
    ["The Lord of the Rings: The Two Towers", "fantasy", "Elijah Wood", 2002],
    ["The Lord of the Rings: The Return of the King", "fantasy", "Elijah Wood", 2003],
    ["Pulp Fiction", "crime", "John Travolta", 1994],
    ["Fight Club", "drama", "Brad Pitt", 1999],
    ["The Godfather", "crime", "Marlon Brando", 1972],
    ["The Empire Strikes Back", "action", "Mark Hamill", 1980],
    ["The Shawshank Redemption", "drama", "Tim Robbins", 1994],
    ["The Dark Knight", "action", "Christian Bale", 2008],
    ["The Lord of the Rings: The Fellowship of the Ring", "fantasy", "Elijah Wood", 2001],
    ["Inglourious Basterds", "war", "Brad Pitt", 2009],
    ["The Shawshank Redemption", "drama", "Tim Robbins", 1994],
]




colonnes = ["Titre", "Genre", "Acteur principal", "Annee"]


df = pd.DataFrame(films, columns=colonnes)


df.to_csv("films.csv", index=False)


df = pd.read_csv("films.csv", encoding="latin-1")


questions = {
    "Genre": ["Tous", "fantastique", "drame", "science-fiction", "thriller", "animation", "autre"],
    "Acteur principal": ["Tous"] + list(df["Acteur principal"].unique()),
    "Période": ["Toutes"] + [f"{annee}-{annee+9}" for annee in range(df['Annee'].min(), df['Annee'].max() + 1, 10)],
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form["genre"]
        acteur = request.form["acteur"]
        periode = request.form["periode"]
        df_filtered = filtrer(genre, acteur, periode)
        return render_template("resultat.html", films=df_filtered)
    return render_template("index.html", questions=questions)


def filtrer(genre, acteur, periode):

    df_filtered = df.copy()
    if genre != "Tous":
        df_filtered = df_filtered.loc[df_filtered["Genre"] == genre]
    if acteur != "Tous":
        df_filtered = df_filtered.loc[df_filtered["Acteur principal"] == acteur]
    if periode != "Toutes":
        years = periode.split('-')
        df_filtered = df_filtered.loc[(df_filtered["Annee"] >= int(years[0])) & (df_filtered["Annee"] <= int(years[1]))]
    return df_filtered

if __name__ == "__main__":
    app.run(debug=True)



