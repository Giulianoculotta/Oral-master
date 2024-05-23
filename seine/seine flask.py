import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

df = pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\seine\\diversite-des-poissons-dans-la-seine.csv", encoding="latin-1")

df.drop(df.columns[0],axis=1 ,inplace=True)
df.drop(df.columns[4],axis=1 ,inplace=True)
df.drop(df.columns[4],axis=1 ,inplace=True)
df.drop(df.columns[0],axis=1 ,inplace=True)
df.drop(df.columns[1],axis=1 ,inplace=True)

df.to_csv("seine.csv", index=False)


df = pd.read_csv("seine.csv", encoding="latin-1")


questions = {
    "station": ["Toutes"] + list(df["nom_station_commune"].unique()),
    "espece": ["Toutes"] + list(df["espece"].unique()),
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        station = request.form["station"]
        espece = request.form["espece"]
        df_filtered = filtrer(station,espece)
        print (df_filtered)
        return render_template("resultat.html", poisson=df_filtered)
    return render_template("Index.html", questions=questions)


def filtrer(station, espece):

    df_filtered = df.copy()
    if station != "Toutes":
        df_filtered = df_filtered.loc[df_filtered["nom_station_commune"] == station]
    if espece != "Toutes":
        df_filtered = df_filtered.loc[df_filtered["espece"] == espece]
    return df_filtered

if __name__ == "__main__":
    app.run(debug=True)



