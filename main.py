from funkcije import *
import time
import pandas as pd

# Glavna zanka 
# Uporabimo funckije iz funkcije.py da zberemo vse potrebne podatke in jih nato shranimo v csv

vsi_animeji = []

for limit in range(0, 1000, 50): # 20 strani (0 do 950) kar nam da 1000 animejev
    print(f"pridobivam stran od mesta {limit + 1}...")
    url = f"https://myanimelist.net/topanime.php?limit={limit}"
    soup = url_v_soup(url)

    # Osnovni podatki iz lestvice
    animeji = Razcleni_stran(soup)

    # Dodatni podatki s podrobnih strani
    for anime in animeji:
        podrobnosti = preberi_podrobnosti(anime["povezava"])
        anime.update(podrobnosti) # Združi oba slovarja
        vsi_animeji.append(anime)

        time.sleep(1) # Majhna pavza da ne obremenjujemo strežnika


# Shranimo podatke
df = pd.DataFrame(vsi_animeji)
df.to_csv("mal_top_1000.csv", index=False, encoding="utf-8-sig")
print("Podatki shranjeni!")
