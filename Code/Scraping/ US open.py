from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

lista_link=[ "https://www.flashscore.com/tennis/atp-singles/us-open-2023/results/",
           "https://www.flashscore.com/tennis/atp-singles/us-open-2022/results/", "https://www.flashscore.com/tennis/atp-singles/us-open-2021/results/",
           "https://www.flashscore.com/tennis/atp-singles/us-open-2020/results/", "https://www.flashscore.com/tennis/atp-singles/us-open-2019/results/",
           "https://www.flashscore.com/tennis/atp-singles/us-open-2018/results/", "https://www.flashscore.com/tennis/atp-singles/us-open-2017/results/",
           "https://www.flashscore.com/tennis/atp-singles/us-open-2016/results/", "https://www.flashscore.com/tennis/atp-singles/us-open-2015/results/",
           "https://www.flashscore.com/tennis/atp-singles/us-open-2014/results/"]

prova=["https://www.flashscore.com/tennis/atp-singles/australian-open-2024/results/", "https://www.flashscore.com/tennis/atp-singles/australian-open-2023/results/",
           "https://www.flashscore.com/tennis/atp-singles/australian-open-2022/results/"]

tutte_partite = {}
def scrape_ausopen_matches():
    for url in lista_link:
        # Imposta il driver di Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)
    
        # Attendi che la pagina si carichi completamente
        wait = WebDriverWait(driver, 40)
    
        anno = driver.find_element(By.CLASS_NAME, "heading__info").text
        anno = int(anno)
        tutte_partite[anno] = []
        players=[]
        games = driver.find_elements(By.CSS_SELECTOR, 'div[id^=g_2]')
        i=1
        for game in games:
            
            partita = {}
            #Definire tipo di partita in base all'indice di iterazione
            if i == 1:
                partita['match type'] = 'Final'
            elif 1 < i < 4:
                partita['match type'] = 'Semi-final'
            elif 3 < i < 8:
                partita['match type'] = 'Quarter-Final'
            elif 7 < i < 16:
                partita['match type'] = '1/8 Final'
            elif 15 < i < 32:
                partita['match type'] = '1/16 Final'
            elif 31 < i < 64:
                partita['match type'] = '1/32 Final'
            else:
                partita['match type'] = '1/64 Final'
            
            
            pl1_elements = game.find_elements(By.CLASS_NAME, 'event__participant--home')
            pl2_elements = game.find_elements(By.CLASS_NAME, 'event__participant--away')
        
            pl1 = pl1_elements[0].text if pl1_elements else ""
            pl2 = pl2_elements[0].text if pl2_elements else ""
            score_player1_elements = game.find_elements(By.CSS_SELECTOR, 'div[class^="event__part event__part--home"]')
            score_player2_elements = game.find_elements(By.CSS_SELECTOR, 'div[class^="event__part event__part--away"]')
        
            score_player1 = []
            score_player2 = []
            
            partita['player1'] = pl1
            partita['player2'] = pl2
        
            for s in score_player1_elements:
                scores = s.text.split('\n')
                if len(scores) > 1:
                    formatted_score = f"{scores[0]}({scores[1]})"
                else:
                    formatted_score = scores[0]
                score_player1.append(formatted_score)
        
            for s in score_player2_elements:
                scores = s.text.split('\n')
                if len(scores) > 1:
                    formatted_score = f"{scores[0]}({scores[1]})"
                else:
                    formatted_score = scores[0]
                score_player2.append(formatted_score)
            
            setW_p1 = game.find_elements(By.CSS_SELECTOR, 'div[class^="event__score event__score--home"]')
            setW_p2 = game.find_elements(By.CSS_SELECTOR, 'div[class^="event__score event__score--away"]')
            if setW_p1[0].text == '-':
                partita['winner'] = 'WO'
            else:
                Sets_p1 = int(setW_p1[0].text) if setW_p1 else ""
                Sets_p2 = int(setW_p2[0].text) if setW_p2 else ""
                partita['points_p1'] = score_player1
                partita['points_p2'] = score_player2
                if Sets_p1 > Sets_p2:
                    partita['winner'] = partita['player1']
                else:
                    partita['winner'] = partita['player2']
            
         
     
            tutte_partite[anno].append(partita)
            i+=1
        
        

            
    
    # Chiudi il driver
        driver.quit()




if __name__ == "__main__":
    scrape_ausopen_matches()
    
    with open('matches_USopen.json', 'w') as f:
        json.dump(tutte_partite, f, indent=4)