from flask import Flask, render_template
import requests,json,sys
key= "af0ee50125705c5e3b5898f7638853d5"
app = Flask(__name__)


uconfig = "https://api.themoviedb.org/3/configuration?api_key="+key
utop = "https://api.themoviedb.org/3/movie/top_rated?api_key="+ key +"&page=1"
ucom = "https://api.themoviedb.org/3/movie/upcoming?api_key="+ key +"&page=1"
unow = "https://api.themoviedb.org/3/movie/now_playing?api_key="+ key +"&page=1"


def config(url):
    try:
        jfile = requests.get(url).json()
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    return jfile
    

dicc = {}
def diccionario(url,nombre):
    results = config(url)["results"]
    titulos,poster, votos, overview, adult = [], [], [], [], []
    for i in results:
        titulos.append(i["original_title"])
        poster.append(i["poster_path"])
        votos.append(i["vote_count"])
        overview.append(i["overview"])
        adult.append(i["adult"])
    dicc[nombre] ={"titles":titulos, "poster":poster, "votos":votos, "overview":overview, "adult":adult}
    return dicc

@app.route("/")
def principal():
    images = config(uconfig)["images"]
    diccionario(utop,"top_rated")
    diccionario(ucom,"playing_now")
    diccionario(unow,"upcoming")

    return render_template("app.html", dicc=dicc, images=images)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
    