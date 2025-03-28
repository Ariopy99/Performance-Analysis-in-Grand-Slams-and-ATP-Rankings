# Scraping prima lista (anno 2024)¶

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura il webdriver per Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL della pagina delle classifiche ATP
url = "https://www.atptour.com/en/rankings/singles"

# Naviga alla pagina
driver.get(url)

# Attendere il caricamento della pagina
time.sleep(5)

# Trova tutti gli elementi <ul> con classe 'player-stats'
player_stats_lists = driver.find_elements(By.CLASS_NAME, 'player-stats')

# Estrai tutti gli href dai tag <a> all'interno di questi ul
hrefs = []
for ul in player_stats_lists:
    links = ul.find_elements(By.TAG_NAME, 'a')
    for link in links:
        hrefs.append(link.get_attribute('href'))


# Chiudi il browser
driver.quit()
link_unici=set(hrefs)

len(link_unici)
link_unici = list(link_unici)

# Lista di tuitti i renking dal 2014 al 2023
tutti_link_ranking = ['https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2023-01-02','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2022-01-03',
                      'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2021-01-04', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2020-01-06',
                      'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2019-01-07', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2018-01-01',
                      'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2017-01-02','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2016-01-04', 
                      'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2015-01-05', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2014-01-06','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2024-05-06', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2023-05-08',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2022-05-09', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2021-05-03',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2020-03-16', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2019-05-06',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2018-05-07', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2017-05-08',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2016-05-02', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2015-05-04',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2014-05-05','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2023-08-07', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2022-08-08',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2021-08-02','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2020-08-24',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2019-08-05','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2018-08-06',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2017-08-07','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2016-08-08',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2015-08-03','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2014-08-04', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2023-06-12', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2022-06-06',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2021-06-14','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2020-03-16',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2019-06-10','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2018-06-11',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2017-06-12', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2016-06-06',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2015-06-08','https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2014-06-09']




# Link di tutti i giocatori in top 100 negli ultimi 10 anni
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

lista=link_unici
for url in tutti_link_ranking: 
    link_unici2=[]
# Configura il webdriver per Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Naviga alla pagina
    driver.get(url)

# Attendere il caricamento della pagina
    time.sleep(5)

# Trova tutti gli elementi <ul> con classe 'player-stats'
    player_stats_lists = driver.find_elements(By.CLASS_NAME, 'player-stats')

# Estrai tutti gli href dai tag <a> all'interno di questi ul
    hrefs2 = []
    for ul in player_stats_lists:
        links = ul.find_elements(By.TAG_NAME, 'a')
        for link in links:
            hrefs2.append(link.get_attribute('href'))

# Stampa gli href estratti
    link_unici2=list(set(hrefs2))
    

    lista.extend(link_unici2)
    

# Chiudi il browser
    driver.quit()

lista=set(lista)

len(lista)
lista_new=list(lista)
lista_new



# estrazioone delle informazioni per ogni giocatore

def extract_player_name_from_href(href):
    parts=href.split('/')
    # Divide l'URL in parti usando '/' come delimitatore
    index = parts.index('players')
        # Il nome del giocatore è la parte successiva
    player_name = parts[index + 1]
        # Sostituisci i trattini con spazi e capitalizza ogni parola
    player_name = player_name.replace('-', ' ').title()
    return player_name

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import json

# Configura il webdriver per Chrome

statistiche_giocatori2={}
# URL della pagina delle classifiche ATP
for url in lista_new:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    giocatore={}


# Naviga alla pagina
    driver.get(url)

# Attendere il caricamento della pagina
    time.sleep(5)

# Trova tutti gli elementi <ul> con classe 'player-stats'
    player_stats_lists = driver.find_elements(By.CLASS_NAME, 'personal_details')

 
    for ul in player_stats_lists:
        second_spans=[]
        list_items = ul.find_elements(By.TAG_NAME, 'li')
        for li in list_items:
            spans = li.find_elements(By.TAG_NAME, 'span')
            if len(spans) >1:
                second_spans.append(spans[1].text)

    
    
    nome = extract_player_name_from_href(url)
    idx=second_spans[0].index('.')
    giocatore['year of birth'] = second_spans[0][idx-4:idx]
    
    
    indice_inizio = second_spans[1].find("(")
    indice_fine = second_spans[1].find("kg", indice_inizio)
    peso_metrico = second_spans[1][indice_inizio + 1:indice_fine]
    
    idx_inizio = second_spans[2].find("(")
    idx_fine = second_spans[2].find("cm", idx_inizio)
    altezza_cm = second_spans[2][idx_inizio + 1:idx_fine]

    
    giocatore['weight'] = peso_metrico
    giocatore['height'] = altezza_cm
    giocatore['turned pro'] = second_spans[3]
    giocatore['hand'] = second_spans[7].split(', ')[0]
    giocatore['backhand'] = second_spans[7].split(', ')[1]
    statistiche_giocatori2[nome]=(giocatore)

# Chiudi il browser
    driver.quit()
with open('giocatori_info.json', 'w') as f:
        json.dump(statistiche_giocatori2, f)


import json

with open('giocTORI_info.json', 'w') as f:
        json.dump(statistiche_giocatori2, f)
        
