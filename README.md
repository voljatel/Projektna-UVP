# Projektna-UVP Analiza Top 1000 rated animejev iz MAL
Avtor: Leon Perko
## Uvod
Za projektno nalogo sem analiziral podatke s spletne strani ([My anime list (MAL)](https://myanimelist.net/)), ki je praktično IMDB ampak za anime (japonske animirane serije/filme). Podatki 
## Navodila
Za brezhibno uporabo mora imeti uporabnik naložene naslednje knjižnice:
- pandas
- matplotlib.pyplot
- re
- requests
- bs4
- time
Če želite posodobiti podatke poženite main.py a to bo trajalo 20-30 min saj sem namerno dal pavze da se strežnik ne obremeni in nas blokira. Po končanem postopku izpiše "Podatki shranjeni!" in povozi anime.csv, anime_studii.csv in anime_zvrsti.csv z novimi podatki. Po tem v analiza-podatkov.ipynb zgoraj izberemo opcijo "Clear all outputs" in nato "Run All" da se še analiza posodobi z novimi podatki (Moji komentarji o rezultatih morda ne bodo več relavantni)
## Kratek opis postopka
- V funkcije.py so shranjene vse funkcije za pobiranje podatkov
- S pomočjo teh funkcij main.py pobere podatke s spleta in jih shrani v csv file (anime.csv, anime_studii.csv, anime_zvrsti.csv)
- Tako shranjene podatke nato v Jupiter notebooku analiziramo v analiza-podatkov.ipynb