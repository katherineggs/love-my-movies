import requests,json,sys,csv
key= "af0ee50125705c5e3b5898f7638853d5"
uconfig =  "https://api.themoviedb.org/3/movie/top_rated?api_key="+ key +"&page=1"

def config(url):
    try:
        jfile = requests.get(url).json()
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    return jfile


# print(config(uconfig))
titulos=[]
print(titulos)

for i in config(uconfig)["results"]:
        titulos.append(i["title"])

print(titulos)