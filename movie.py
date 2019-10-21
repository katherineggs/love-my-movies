from flask import Flask, render_template
# from jinja2 import Environment, PackageLoader, select_autoescape
import requests,json,sys,csv
key= "af0ee50125705c5e3b5898f7638853d5"
app = Flask(__name__)
# env = Environment(
#     loader=PackageLoader('movie', 'templates'),
#     autoescape=select_autoescape(['html']),
#     extensions=['jinja2.ext.loopcontrols']
# )

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
    

# with open("discover_movies.json", encoding="utf8") as movie_file:
#     movies = json.load(movie_file)


@app.route("/")
def principal():
    images = config(uconfig)["images"]
    titulos,poster, votos, overview, adult = [], [], [], [], []
    top_results = config(utop)["results"]
    com_results = config(ucom)["results"]
    now_results = config(unow)["results"]
    dicc = {}
    titulos,poster, votos, overview, adult = [], [], [], [], []
    for i in top_results:
        titulos.append(i["title"])
        poster.append(i["poster_path"])
        votos.append(i["vote_count"])
        overview.append(i["overview"])
        adult.append(i["adult"])
    dicc["top_rated"] ={"titles":titulos, "poster":poster, "votos":votos, "overview":overview, "adult":adult}
    
    titulos,poster, votos, overview, adult = [], [], [], [], []
    for i in com_results:
        titulos.append(i["title"])
        poster.append(i["poster_path"])
        votos.append(i["vote_count"])
        overview.append(i["overview"])
        adult.append(i["adult"])
    dicc["upcoming"] = {"titles":titulos, "poster":poster, "votos":votos, "overview":overview, "adult":adult}
    
    titulos,poster, votos, overview, adult = [], [], [], [], []
    for i in now_results:
        titulos.append(i["title"])
        poster.append(i["poster_path"])
        votos.append(i["vote_count"])
        overview.append(i["overview"])
        adult.append(i["adult"])
    dicc["playing_now"] ={"titles":titulos, "poster":poster, "votos":votos, "overview":overview, "adult":adult}

    return render_template("app.html", dicc=dicc, images=images)

if __name__ == "__main__":
    app.run(debug=True)