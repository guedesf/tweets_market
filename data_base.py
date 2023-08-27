## [--DataBase--] ##

## Importacoes
import pandas as pd
from pymongo import MongoClient
from functions import sentiment
from config import nameBD

## Conexao MongoDB
conn = MongoClient('localhost', 27017)

## Instancia MongoDB
db = conn.xpe

## Nome do banco criado
db.name

## Colecoes existentes
db.list_collection_names()

## Numero de registros dentro da colecao
db[nameBD].count_documents({})
db[nameBD].estimated_document_count()

## Recuperar os documentos
docs = db[nameBD].find()

## To dicionario
dataF = [doc for doc in docs]

## Analise de sentimento
for entry in dataF:
    positive = 0
    negative = 0
    neutral = 0
    
    for tweet in entry['Tweets']:
        sentimento = sentiment(tweet['content'])
        tweet['sentiment'] = sentimento
        
        if sentimento == 'positivo':
            positive += 1
        
        elif sentimento == 'negativo':
            negative += 1
        
        else:
            neutral += 1
    
    entry['Positivo'] = positive
    entry['Negativo'] = negative
    entry['Neutro'] = neutral

## Chaves DataFrame
chaves = ['Id_Date', 'Volume', 'Retorno', 
          'Quantidade', 'Positivo', 'Negativo', 'Neutro']

## DataFrame final
dataF = pd.DataFrame([{chave: d[chave] for chave in chaves} for d in dataF])
dataF.to_excel('datasets/'+ nameBD + '/dataF.xlsx', index = False)