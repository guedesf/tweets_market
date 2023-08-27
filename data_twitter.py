## [--Coleta de Dados do Twiter--] ##

## Importacoes
import json
import pandas as pd
from config import emp, nameBD

## DataSet
jsonl_file = 'datasets/twitter.jsonl'

## Lista
data_twitter = []

## Carregando os tweets
with open(jsonl_file, 'r') as f:
    for line in f:
        json_data = json.loads(line)
        
        if 'content' in json_data and emp in json_data['content'].upper():
            data_twitter.append(json_data)
            
## DataFrame
data_twitter = pd.DataFrame(data_twitter)

## Convertendo para datetime
data_twitter['date'] = pd.to_datetime(data_twitter['date'])

## Ordenando por data
data_twitter = data_twitter.sort_values(by = 'date')
data_twitter = data_twitter.reset_index()

## Criando Id_Date
data_twitter['Id_Date'] = data_twitter['date'].dt.day + \
                          data_twitter['date'].dt.month * 100 + \
                          data_twitter['date'].dt.year * 10000

## Reduzindo data_twitter
data_twitter = data_twitter[['Id_Date', 'id', 'date', 'content']]

## Dataframe to csv
data_twitter.to_csv('datasets/' + nameBD + '/tweets.csv', index = False)