from funkcije import *
import time
import pandas as pd

# Glavna zanka 
# Uporabimo funckije iz funkcije.py da zberemo vse potrebne podatke in jih nato shranimo v csv

anime_osnovno = []
anime_studii = []
anime_zvrsti = []

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
        
        # Izlušči id
        anime_id = izlusci_id(anime["povezava"])
        anime["anime id"] = anime_id

        # Shranimo osnovne podatke
        anime_osnovno.append({
            "anime id": anime_id,
            "naslov": anime["naslov"],
            "ocena": anime["ocena"],
            "tip": anime["tip"],
            "število epizod": anime["število epizod"],
            "leto izdaje": anime["leto izdaje"],
            "število članov": anime["število članov"],
        })

        # Shrani zvrsti
        if anime["zvrsti"]: # Samo če seznam ni prazen (popravek napake)
            for z in anime["zvrsti"]:
                anime_zvrsti.append({"anime id": anime_id, "zvrst": z})

        # Shrani studie
        for s in anime["studii"]:
            anime_studii.append({"anime id": anime_id, "studio": s})


        time.sleep(1) # Majhna pavza da ne obremenjujemo strežnika


# Shranimo podatke
pd.DataFrame(anime_osnovno).to_csv("anime.csv", index=False, encoding="utf-8-sig")
pd.DataFrame(anime_zvrsti).to_csv("anime_zvrsti.csv", index=False, encoding="utf-8-sig")
pd.DataFrame(anime_studii).to_csv("anime_studii.csv", index=False, encoding="utf-8-sig")
print("Podatki shranjeni!")
