import re
import requests
from bs4 import BeautifulSoup
import time



def Url_v_soup(url1):
    # Iz URL-ja vrne Beautifulsoup #
    headers = {"User-Agent": "Mozilla/5.0"} # Se pretvarja da je brskalnik da prepreči blokiranje #
    html = requests.get(url1, headers=headers)
    html.raise_for_status()
    return BeautifulSoup(html.text, "html.parser")


# Funkcije ki izluščijo določene podatke iz prvotne strani #

def izlusci_naslov(vrstica):
    # Iz vrstive izlušči naslov Animeja #
    oznaka_naslova = vrstica.find("h3", class_="anime_ranking_h3").find("a")
    return oznaka_naslova.text.strip()

def izlusci_link(vrstica):
    # Iz vrstice izlušči link do strani s podrobnejšimi podatki o animeju #
    oznaka_naslova = vrstica.find("h3", class_="anime_ranking_h3").find("a")
    return oznaka_naslova["herf"]

def izlusci_oceno(vrstica):
    # Iz vrstice izlušči oceno animeja #
    oznaka_ocene = vrstica.find("div", class_="js-top-ranking-score-col")
    if oznaka_ocene:
        return oznaka_ocene.text.strip()
    else:
        return None
    
def Razcleni_stran(soup):
    # Razčleni eno stran lestvice in vrne seznam slovarjev (naslov, link, ocena) #
    animeji = []
    vrstice = soup.find_all("tr", class_="ranking-list")
    for vrstica in vrstice:
        animeji.append({
            "naslov": izlusci_naslov(vrstica),
            "link": izlusci_link(vrstica),
            "ocena": izlusci_oceno(vrstica),
        })
    return animeji







