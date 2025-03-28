link_10anni = ['https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2024-05-06', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2023-05-08',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2022-05-09', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2021-05-03',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2020-03-16', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2019-05-06',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2018-05-07', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2017-05-08',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2016-05-02', 'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2015-05-04',
              'https://www.atptour.com/en/rankings/singles?RankRange=0-100&Region=all&DateWeek=2014-05-05']



import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Imposta il path del ChromeDriver (sostituisci con il path corretto sul tuo sistema)

ranking_10anni={}
def scrape_atp_rankings():
    # Inizializza il WebDriver
    
    
    i=2024

    for link in link_10anni: 
        # Naviga alla pagina desiderata
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(link)

        # Attendi che la tabella dei giocatori sia caricata
        wait = WebDriverWait(driver, 40)
        
         

            # Estrai i dati
        players = driver.find_elements(By.CSS_SELECTOR, "tr.lower-row")

            # Inizializza una lista per salvare i dati
        player_data = []

        for player in players:
                try:

                    ranking = player.find_element(By.CLASS_NAME, "rank.bold.heavy.tiny-cell").text
                    name = player.find_element(By.CSS_SELECTOR, 'a[href^="/en/players"]').text
                    
                    if name != '':




                            player_data.append({
                            "Name":name,
                            "Rank": ranking
                        })
                except NoSuchElementException as e:
                    print(f"Errore nel trovare un elemento: {e}")

            # Stampa i dati estratti
        ranking_10anni[i]=player_data
        i=i-1
        driver.quit()


if __name__ == "__main__":
    scrape_atp_rankings()
    
    with open('rank_FRENCH.json', 'w') as f:
        json.dump(ranking_10anni, f, indent=4)
