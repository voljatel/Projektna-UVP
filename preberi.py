import re
import requests
from bs4 import BeautifulSoup
import time



def Url_v_soup(url):
    # Iz URL-ja vrne Beautifulsoup 
    headers = {"User-Agent": "Mozilla/5.0"} # Se pretvarja da je brskalnik da prepreči blokiranje 
    html = requests.get(url, headers=headers)
    html.raise_for_status()
    return BeautifulSoup(html.text, "html.parser")


# Funkcije ki izluščijo določene podatke iz prvotne strani 

def izlusci_naslov(vrstica):
    # Iz vrstive izlušči naslov Animeja 
    oznaka_naslova = vrstica.find("h3", class_="anime_ranking_h3").find("a")
    return oznaka_naslova.text.strip()

def izlusci_link(vrstica):
    # Iz vrstice izlušči link do strani s podrobnejšimi podatki o animeju 
    oznaka_naslova = vrstica.find("h3", class_="anime_ranking_h3").find("a")
    return oznaka_naslova["herf"]

def izlusci_oceno(vrstica):
    # Iz vrstice izlušči oceno animeja 
    oznaka_ocene = vrstica.find("div", class_="js-top-ranking-score-col")
    if oznaka_ocene:
        return oznaka_ocene.text.strip()
    else:
        return None
    
def Razcleni_stran(soup):
    # Razčleni eno stran lestvice in vrne seznam slovarjev (naslov, link, ocena) 
    animeji = []
    vrstice = soup.find_all("tr", class_="ranking-list")
    for vrstica in vrstice:
        animeji.append({
            "naslov": izlusci_naslov(vrstica),
            "link": izlusci_link(vrstica),
            "ocena": izlusci_oceno(vrstica),
        })
    return animeji


# Funkcije za izluščanje podrobnejših podatkov iz strani posameznega animeja 

def izlusci_studie(soup):
    # Izlušči studie 
    studii = []
    oznaka_studia = soup.find("span", string= "Studios:")
    if oznaka_studia:
        for a in oznaka_studia.find_next_siblings("a"):
            studii.append(a.text.strip())
    return studii

def izlusci_tip(soup):
    # Izlusci tipe (TV, Movie, OVA, ...)
    oznaka_tipa = soup.find("span", string="Type:")
    if oznaka_tipa:
        return oznaka_tipa.find_next("a").text.strip()
    else:
        return None

def izlusci_epizode(soup):
    # izlušči število epizod 
    oznaka_ep = soup.find("span", string= "Episodes:")
    if oznaka_ep:
        return oznaka_ep.next_sibling.strip()
    else:
        return None

def izlusci_zvrsti(soup):
    # Izlušči zvrsti
    zvrsti = []
    oznaka_zvrst = soup.find("span", string="Genres:")
    if oznaka_zvrst:
        for a in oznaka_zvrst.find_next_siblings("a"):
            zvrsti.append(a.text.strip())
    return zvrsti

def izlusci_leto(soup):
    # Izlošči leto prve izdaje animeja
    oznaka_premiere = soup.find("span", string="Aired:")
    if oznaka_premiere: 
        text = oznaka_premiere.next_sibling.strip()
        # Poiščemo prvo 4 mestno število (leto)
        match = re.search(r"\b(\d{4})\b", text)
        if match:
            return int(match.group(1))
        else:
            return None








