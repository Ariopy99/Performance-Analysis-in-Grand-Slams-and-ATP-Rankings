from pymongo import MongoClient

# Connessione al database MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['Tennis'] 
Wimb = db['Wimbledon']

import json

with open('match_Wimbledon_new.json', 'r') as file:
    matches = json.load(file)

for anno in matches:
    for partita in matches[str(anno)]:
        Wimb.insert_one(partita)

with open('rank_W_new.json', 'r') as file:
    r_W = json.load(file)

rank = db['rank Wimbledon']
for anno in r_W:
    for giocatore in r_W[str(anno)]:
        giocatore['year']=anno
        rank.insert_one(giocatore)

for giocatore in rank.find():
    name=giocatore['Name'].replace("-", " ")
    name=name.title()
    rank.update_one({'_id': giocatore['_id']},
            {'$set': {'Name':name}})

# Integration

players=db['Overview']
overview_data = players.find_one()


# Trasforma overview_data in un dizionario per una ricerca veloce
overview_dict = {}
for player, details in overview_data.items():
    if player != '_id':  # Ignora il campo _id
        overview_dict[player] = details

for doc in rank.find():
    player_name = doc['Name']
    if player_name in overview_dict:
        birth = overview_dict[player_name].get('year of birth')
        weight = overview_dict[player_name].get('weight')
        height = overview_dict[player_name].get('height')
        pro = overview_dict[player_name].get('turned pro')
        hand = overview_dict[player_name].get('hand')
        backhand = overview_dict[player_name].get('backhand')
        rank.update_one(
            {'_id': doc['_id']},
            {'$set': {'year of birth': birth,'weight':weight,'height':height,'turned pro': pro,'hand': hand, 'backhand': backhand}}
        )


for giocatore in rank.find():
    if 'hand' not in giocatore:
        print(giocatore)

#integrazione con i match

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['Tennis'] 
rank_collection = db['rank Wimbledon']
match_collection = db['Wimbledon']

from bson import ObjectId
for giocatore in rank_collection.find():
    if giocatore['Name']=='Alexander Zverev':
        chiave=ObjectId(giocatore['_id'])
        rank_collection.update_one({'_id': chiave},
            {'$set': {'Name Formatted': 'Zverev A.'}})

rank_data = list(rank_collection.find())
for player in rank_data:
    if 'Name Formatted' not in player:
        print(player)

from bson import ObjectId
document_id = '668a9c5de169e56598eae120'  # Sostituire con l'ID del documento

# Convertire l'ID in ObjectId se necessario
try:
    document_id = ObjectId(document_id)
except Exception as e:
    print(f"ID non valido: {e}")
    exit()

rank_collection.update_one({'_id': document_id}, {'$set': {'Name Formatted': 'Ramos A.'}})

rank_collection.update_one({'_id': ObjectId('668a9c5de169e56598eae121')}, {'$set': {'Name Formatted': 'van Assche L.'}})

rank_data = list(rank_collection.find()) #Lista con tutti i documenti di rank
# Creare un dizionario per mappare i giocatori in base al loro "Name Formatted" e "year"
rank_dict = {}
for player in rank_data:
    key = (player['Name Formatted'], player['year'])
    rank_dict[key] = player
rank_dict

# Recuperare i dati dalla collezione match
matches = list(match_collection.find())

# Funzione per trovare il nome del giocatore considerando l'anno
def find_player(name_formatted, year):
    # Cerca nel dizionario usando il metodo get, specificando un valore di default se la chiave non viene trovata
    player_data = rank_dict.get((name_formatted, year), None)
    
    # Se il valore di ritorno è None, genera il dizionario con i dati di default
    if player_data is None:
        return {'Name': name_formatted, 'Rank': 'Not in Top 100'}
    
    # Altrimenti, ritorna il dato trovato
    return player_data


for match in matches:
    year = match['year']
    player1_formatted = match['player1']
    player2_formatted = match['player2']
    
    match['player1'] = find_player(player1_formatted, year)
    match['player2'] = find_player(player2_formatted, year)
    
    # Aggiornare il documento nel database
    match_collection.update_one({'_id': match['_id']}, {'$set': match})

# Chiudere la connessione a MongoDB
client.close()