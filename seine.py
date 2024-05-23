import tkinter as tk
import pandas as pd
import os
from tkinter import ttk

os.environ['DISPLAY'] = ':0.0'  
# Lire le fichier CSV
df = pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\seine\\diversite-des-poissons-dans-la-seine.csv", encoding="latin-1")

df.drop(df.columns[0],axis=1 ,inplace=True)
df.drop(df.columns[4],axis=1 ,inplace=True)
df.drop(df.columns[4],axis=1 ,inplace=True)
df.drop(df.columns[0],axis=1 ,inplace=True)
df.drop(df.columns[1],axis=1 ,inplace=True)
# Définition des questions et des choix possibles
questions = {
    "station": ["Toutes"] + list(df["nom_station_commune"].unique()),
    "espece": ["Toutes"] + list(df["espece"].unique()),
}


var_periode = None
var_station = None
var_espece = None
fenetre_principale = None

def filtrer():

    station = var_station.get()
    espece = var_espece.get()

    

    df_filtered = df.copy()
    if station != "Toutes":
        df_filtered = df_filtered.loc[df_filtered["nom_station_commune"] == station]
    
    if espece != "Toutes":
        df_filtered = df_filtered.loc[df_filtered["espece"] == espece]
    


    print(df_filtered)



def affiner_recherche(df):
    global fenetre_principale

    if fenetre_principale is not None:
        fenetre_principale.destroy()
    

    fenetre_principale = tk.Tk()
    fenetre_principale.title("Recherche avancée")
    
    global var_station, var_espece
    

    for i, (question, options) in enumerate(questions.items()):
        # Label de la question
        label = ttk.Label(fenetre_principale, text=f"{question}:")
        label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
        

        var = tk.StringVar(fenetre_principale)
        var.set("Toutes")
        menu = ttk.Combobox(fenetre_principale, textvariable=var, values=options)
        menu.grid(row=i, column=1, padx=5, pady=5, sticky="ew")
        

        if question == "station":
            var_station = var
        elif question == "espece":
            var_espece = var



        ttk.Separator(fenetre_principale, orient='horizontal')

    
    filtrer_button = ttk.Button(fenetre_principale, text="Filtrer", command=filtrer)
    filtrer_button.grid(row=len(questions), columnspan=2, padx=5, pady=10)

   
    for i in range(len(questions) + 1):
        fenetre_principale.grid_rowconfigure(i, weight=1)
    fenetre_principale.grid_columnconfigure(0, weight=1)
    fenetre_principale.grid_columnconfigure(1, weight=1)


    fenetre_principale.mainloop()



affiner_recherche(df)