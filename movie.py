from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
import requests,json

app = Flask(__name__)
# env = Environment(
#     loader=PackageLoader('movie', 'templates'),
#     autoescape=select_autoescape(['html']),
#     extensions=['jinja2.ext.loopcontrols']
# )

with open("discover_movies.json", encoding="utf8") as movie_file:
    movies = json.load(movie_file)


@app.route("/")
def principal():
    titulos=[] 
    poster=[]
    votos=[]
    overview=[]  
    for i in movies["results"]:
        titulos.append(i["title"])
        poster.append(i["poster_path"])
        votos.append(i["vote_count"])
        overview.append(i["overview"])
    return render_template("app.html", titulos=titulos, poster=poster, votos=votos, overview=overview)

if __name__ == "__main__":
    app.run(debug=True)