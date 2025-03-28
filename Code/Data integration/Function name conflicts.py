def converti(rank,match):
    nomi_giusti=[]
    
    for anno in range(2014,2025):
        if str(anno) in match:
            for lista_partite in match[str(anno)]:
                nomi_giusti.append(lista_partite['player1'])
                nomi_giusti.append(lista_partite['player2'])
    nomi_giusti=list(set(nomi_giusti))

    diz_giusti={}
    for i in range(0,len(nomi_giusti)):
            if len(nomi_giusti[i].split(' '))==2:
                diz_giusti[nomi_giusti[i].split(' ')[0]]=nomi_giusti[i]
            elif len(nomi_giusti[i].split(' '))==3:
                diz_giusti[nomi_giusti[i].split(' ')[0]+' '+nomi_giusti[i].split(' ')[1]]=nomi_giusti[i]
            elif len(nomi_giusti[i].split(' '))==4:
                diz_giusti[nomi_giusti[i].split(' ')[0]+' '+nomi_giusti[i].split(' ')[1]+' '+nomi_giusti[i].split(' ')[2]]=nomi_giusti[i]

    for anno in range(2014,2025):
        if str(anno) in rank:
                for giocatore in rank[str(anno)]:
                    nome_sb=giocatore['Name']
                    parti=nome_sb.split(' ')
                    if len(parti)==2:
                        if parti[1] in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[parti[1]]
                        else:
                            cognome=parti[1].replace("-", " ")
                            if cognome in diz_giusti:
                                giocatore['Name Formatted']=diz_giusti[cognome]
                    elif len(parti)==3:
                        parti = [parte.capitalize() for parte in parti]
                        poss1=parti[1]+' '+parti[2]
                        poss2=parti[2]
                        poss3=parti[1]+'-'+parti[2]
                        poss4=parti[2]+' '+parti[0][0]+'.'

                        if poss1 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss1]
                        elif poss2 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss2]
                        elif poss3 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss3]
                        elif poss4 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss4]

                    elif len(parti)==4:
                        parti = [parte.capitalize() for parte in parti]
                        poss1=parti[2]+' '+parti[3]
                        poss2=parti[3]
                        poss3=parti[1]+' '+parti[2]+' '+parti[3]
                        if poss1 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss1]
                        elif poss2 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss2]
                        elif poss3 in diz_giusti:
                            giocatore['Name Formatted']=diz_giusti[poss3]
                    
                
            
    
    return rank


### AUS OPEN

import json

# Carica il contenuto del file JSON
with open('rank_AUS.json', 'r') as file:
    rank_AUS = json.load(file)


with open('matches_AUS.json', 'r') as file:
    match_AUS = json.load(file)

with open('rank_AUS_new.json', 'w') as f:
        json.dump(converti(rank_AUS, match_AUS), f, indent=4)


with open('rank_AUS_new.json', 'r') as file:
    prova = json.load(file)
for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if 'Name Formatted' not in giocatore:
            print(giocatore['Name'])



for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if giocatore['Name']=='Albert Ramos-Vinolas':
            giocatore['Name Formatted']='Ramos A.'
        elif giocatore['Name']=='Alex Bogomolov Jr.':
            giocatore['Name Formatted']='Bogomolov A. Jr'
        elif giocatore['Name']=='Victor Estrella Burgos':
            giocatore['Name Formatted']='Estrella V.'
        elif giocatore['Name']=='Daniel Munoz de la Nava':
            giocatore['Name Formatted']='Munoz-De La Nava D.'
        elif giocatore['Name']=='Rogerio Dutra Silva':
            giocatore['Name Formatted']='Silva D. R.'   
with open('rank_AUS_new.json', 'w') as f:
        json.dump(prova, f, indent=4)



### ROLLAND GARROS

# Carica il contenuto del file JSON
with open('rank_FRENCH.json', 'r') as file:
    rank_F = json.load(file)


with open('matches_French.json', 'r') as file:
    match_F = json.load(file)

with open('rank_F_new.json', 'w') as f:
        json.dump(converti(rank_F, match_F), f, indent=4)

with open('rank_F_new.json', 'r') as file:
    prova = json.load(file)
for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if 'Name Formatted' not in giocatore:
            print(giocatore['Name'])
    

for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if giocatore['Name']=='Albert Ramos-Vinolas':
            giocatore['Name Formatted']='Ramos A.'
        elif giocatore['Name']=='Alex Bogomolov Jr.':
            giocatore['Name Formatted']='Bogomolov A. Jr'
        elif giocatore['Name']=='Victor Estrella Burgos':
            giocatore['Name Formatted']='Estrella V.'
        elif giocatore['Name']=='Daniel Munoz de la Nava':
            giocatore['Name Formatted']='Munoz-De La Nava D.'
        elif giocatore['Name']=='Rogerio Dutra Silva':
            giocatore['Name Formatted']='Silva D. R.' 
        elif giocatore['Name']=='Luca Van Assche':
            giocatore['Name Formatted']='van Assche L.' 
with open('rank_F_new.json', 'w') as f:
        json.dump(prova, f, indent=4)



### WIMBLEDON

# Carica il contenuto del file JSON
with open('rank_WIMB.json', 'r') as file:
    rank_W = json.load(file)


with open('matches_Wimbledon.json', 'r') as file:
    match_W = json.load(file)
    
with open('rank_W_new.json', 'w') as f:
        json.dump(converti(rank_W, match_W), f, indent=4)

with open('rank_W_new.json', 'r') as file:
    prova = json.load(file)
for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if 'Name Formatted' not in giocatore:
            print(giocatore['Name'])

for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if giocatore['Name']=='Albert Ramos-Vinolas':
            giocatore['Name Formatted']='Ramos A.'
        elif giocatore['Name']=='Alex Bogomolov Jr.':
            giocatore['Name Formatted']='Bogomolov A. Jr'
        elif giocatore['Name']=='Victor Estrella Burgos':
            giocatore['Name Formatted']='Estrella V.'
        elif giocatore['Name']=='Daniel Munoz de la Nava':
            giocatore['Name Formatted']='Munoz-De La Nava D.'
        elif giocatore['Name']=='Rogerio Dutra Silva':
            giocatore['Name Formatted']='Silva D. R.' 
        elif giocatore['Name']=='Luca Van Assche':
            giocatore['Name Formatted']='van Assche L.' 
        elif giocatore['Name']=='Andrej Martin':
            giocatore['Name Formatted']='Martin A.'
with open('rank_W_new.json', 'w') as f:
        json.dump(prova, f, indent=4)



### US OPEN

# Carica il contenuto del file JSON
with open('rank_US.json', 'r') as file:
    rank_US = json.load(file)


with open('matches_USopen.json', 'r') as file:
    match_US = json.load(file)


with open('rank_US_new.json', 'w') as f:
        json.dump(converti(rank_US, match_US), f, indent=4)

with open('rank_US_new.json', 'r') as file:
    prova = json.load(file)
for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if 'Name Formatted' not in giocatore:
            print(giocatore['Name'])

for anno in range(2014,2024):
    for giocatore in prova[str(anno)]:
        if giocatore['Name']=='Albert Ramos-Vinolas':
            giocatore['Name Formatted']='Ramos A.'
        elif giocatore['Name']=='Alex Bogomolov Jr.':
            giocatore['Name Formatted']='Bogomolov A. Jr'
        elif giocatore['Name']=='Victor Estrella Burgos':
            giocatore['Name Formatted']='Estrella V.'
        elif giocatore['Name']=='Daniel Munoz de la Nava':
            giocatore['Name Formatted']='Munoz-De La Nava D.'
        elif giocatore['Name']=='Rogerio Dutra Silva':
            giocatore['Name Formatted']='Silva D. R.' 
        elif giocatore['Name']=='Luca Van Assche':
            giocatore['Name Formatted']='van Assche L.' 
        elif giocatore['Name']=='Andrej Martin':
            giocatore['Name Formatted']='Martin A.'
        elif giocatore['Name']=='Chun-Hsin Tseng':
            giocatore['Name Formatted']='Tseng C. H.'
        elif giocatore['Name']=='Jurgen Zopp':
            giocatore['Name Formatted']='Zopp J.'
with open('rank_US_new.json', 'w') as f:
        json.dump(prova, f, indent=4)


