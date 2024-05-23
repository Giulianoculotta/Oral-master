import tkinter as tk
import pandas as pd
import os
from tkinter import ttk





os.environ['DISPLAY'] = ':0.0'  


""" Liste des films"""
films = [
    ["Le Seigneur des Anneaux : Le Retour du Roi", "fantastique", "Elijah Wood", 2003],
    ["Le Parrain", "drame", "Marlon Brando", 1972],
    ["Inception", "science-fiction", "Leonardo DiCaprio", 2010],
    ["Star Wars : Épisode IV - Un nouvel espoir", "science-fiction", "Mark Hamill", 1977],
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
    ["The Godfather: Part II", "crime", "Al Pacino", 1974],
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


var_genre = None
var_acteur = None
var_periode = None
fenetre_principale = None


def filtrer():

    genre = var_genre.get()
    acteur = var_acteur.get()
    periode = var_periode.get()
    

    df_filtered = df.copy()
    if genre != "Tous":
        df_filtered = df_filtered.loc[df_filtered["Genre"] == genre]
    
    if acteur != "Tous":
        df_filtered = df_filtered.loc[df_filtered["Acteur principal"] == acteur]
    
    if periode != "Toutes":
        years = periode.split('-')
        df_filtered = df_filtered.loc[(df_filtered["Annee"] >= int(years[0])) & (df_filtered["Annee"] <= int(years[1]))]
    
    # Afficher les résultats
    print(df_filtered)


def affiner_recherche(df):
    global fenetre_principale

    if fenetre_principale is not None:
        fenetre_principale.destroy()
    

    fenetre_principale = tk.Tk()
    fenetre_principale.title("Recherche avancée")
    
    global var_genre, var_acteur, var_periode
    

    for i, (question, options) in enumerate(questions.items()):

        label = ttk.Label(fenetre_principale, text=f"{question}:")
        label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
        

        var = tk.StringVar(fenetre_principale)
        var.set("Tous" if question != "Période" else "Toutes")  
        menu = ttk.Combobox(fenetre_principale, textvariable=var, values=options)
        menu.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
        

        if question == "Genre":
            var_genre = var
        elif question == "Acteur principal":
            var_acteur = var
        elif question == "Période":
            var_periode = var


        ttk.Separator(fenetre_principale, orient='horizontal')


    filtrer_button = ttk.Button(fenetre_principale, text="Filtrer", command=filtrer)
    filtrer_button.grid(row=len(questions), columnspan=2, padx=5, pady=10)

   
    for i in range(len(questions) + 1):
        fenetre_principale.grid_rowconfigure(i, weight=1)
    fenetre_principale.grid_columnconfigure(0, weight=1)
    fenetre_principale.grid_columnconfigure(1, weight=1)

    fenetre_principale.mainloop()



affiner_recherche(df)