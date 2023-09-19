## [--DataAnalytics--] ##

## Importacoes
import pandas as pd
from functions import grafico_barras, matiz_corr
from config import nameBD

## DataSet
diretorio = 'datasets/' + nameBD 
data = pd.read_excel(diretorio + '/dataF_' + nameBD + '.xlsx')

## Ordenando por quantidade
data = data.sort_values(by = 'Quantidade', 
                        ascending = False).reset_index(drop = True)

## 40 maiores quantidades
data = data.head(40)

## Ordenando por data
data = data.sort_values(by = 'Id_Date').reset_index(drop = True)

## Negativando coluna
data['Negativo'] = data['Negativo'] * -1

## Retorno em percentual
data['Retorno'] = data['Retorno'] * 100

## Percentual de mencoes
data['Per_Neutro'] = data['Neutro'] / data['Quantidade']
data['Per_Negativo'] = data['Negativo'] / data['Quantidade']
data['Per_Positivo'] = data['Positivo'] / data['Quantidade']

## Matriz de correlacao
matiz_corr(data)

## Grafico de barras
grafico_barras(data)