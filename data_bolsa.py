## [--Coleta de Dados da Bovespa--] ##

## Importacoes
from functions import bolsa
from config import tiks, nameBD

## Dados da consulta
tickers = [tiks]
start_date = '2013-12-06'
end_date = '2019-06-30'

## DataFrame
data_bolsa = bolsa(tickers, start_date, end_date)
data_bolsa = data_bolsa.reset_index()

## Ordenando por data
data_bolsa = data_bolsa.sort_values(by = 'Date')

## Criando Id_Date
data_bolsa['Id_Date'] = data_bolsa['Date'].dt.day + \
                        data_bolsa['Date'].dt.month * 100 + \
                        data_bolsa['Date'].dt.year * 10000

## Adicionando variacao
data_bolsa['Variacao'] = data_bolsa['Close'].diff()
data_bolsa['Retorno'] = data_bolsa['Variacao'] / data_bolsa['Close'].shift(1)  

## Reduzindo data_bolsa
data_bolsa = data_bolsa[['Id_Date', 'Date', 'Ticker', 'Volume', 'Retorno']]

## Removendo NaN
data_bolsa.dropna(subset = ['Retorno'], inplace = True)

## Resetar o index
data_bolsa.reset_index(drop = True, inplace = True)

## Dataframe to csv
data_bolsa.to_csv('datasets/' + nameBD +'/bolsa.csv', index = False)