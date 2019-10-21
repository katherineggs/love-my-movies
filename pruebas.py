import requests,json,sys,csv
key= "af0ee50125705c5e3b5898f7638853d5"
uconfig =  "https://api.themoviedb.org/3/movie/top_rated?api_key="+ key +"&page=1"
utop = "https://api.themoviedb.org/3/movie/top_rated?api_key="+ key +"&page=1"
upop = "https://api.themoviedb.org/3/movie/upcoming?api_key="+ key +"&page=1"
unow = "https://api.themoviedb.org/3/movie/now_playing?api_key="+ key +"&page=1"

def config(url):
    try:
        jfile = requests.get(url).json()
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    return jfile


titulos,poster, votos, overview, adult = [], [], [], [], []
top_results = config(utop)["results"]
com_results = config(upop)["results"]
now_results = config(unow)["results"]
dicc = {}
titulos,poster, votos, overview, adult = [], [], [], [], []
for i in top_results:
    titulos.append(i["title"])
    poster.append(i["poster_path"])
    votos.append(i["vote_count"])
    adult.append(i["adult"])
dicc["top_rated"] ={"titles":titulos, "poster":poster, "votos":votos, "adult":adult}

titulos,poster, votos, overview, adult = [], [], [], [], []
for i in com_results:
    titulos.append(i["title"])
    poster.append(i["poster_path"])
    votos.append(i["vote_count"])
    adult.append(i["adult"])
dicc["upcoming"] = {"titles":titulos, "poster":poster, "votos":votos, "adult":adult}

titulos,poster, votos, overview, adult = [], [], [], [], []
for i in now_results:
    titulos.append(i["title"])
    poster.append(i["poster_path"])
    votos.append(i["vote_count"])
    adult.append(i["adult"])
dicc["playing_now"] ={"titles":titulos, "poster":poster, "votos":votos, "adult":adult}


# for k,v in dicc.items():
#     print(k,v,"\n")
top = dicc["top_rated"]
poster= top["poster"]
print(poster)