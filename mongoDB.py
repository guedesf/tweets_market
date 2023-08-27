## [--MongoDB--] ##

## Importacoes
from config import nameBD
from pymongo import MongoClient
from data_bolsa import data_bolsa
from data_twitter import data_twitter

## DataFrames to dicionario
data_bolsa = data_bolsa.to_dict('records')
data_twitter = data_twitter.to_dict('records')

## Dicionario unico
data = []

## Join dos dicionarios
for registro in data_bolsa:
    id_date = registro['Id_Date']
    related = [doc for doc in data_twitter if doc['Id_Date'] == id_date]
    
    if related:
        registro['Quantidade'] = len(related)
        registro['Tweets'] = related
        data.append(registro)

## Conexao MongoDB
conn = MongoClient('localhost', 27017)

## Instancia MongoDB
db = conn.xpe

## Colecao PA MongoDB
collec = db[nameBD]

## Inserindo no MongoDB
for registro in data:
    post_id = collec.insert_one(registro)
    post_id.inserted_id