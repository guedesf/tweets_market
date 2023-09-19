## [--Funcoes e Graficos--] ##

## Importacoes
import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
from config import nameBD

## Diretorio
diretorio = 'datasets/' + nameBD 

## Coleta informacoes NYSE e NASDAQ 
def bolsa(tickers, start_date, end_date):
    
    df_list = []
    for ticker in tickers:
        data = yf.download(ticker, start = start_date, end = end_date)
        
        if not data.empty:
            data['Ticker'] = ticker
            df_list.append(data)
    
    if df_list:
        return pd.concat(df_list)

## Analise de sentimento
def sentiment(tweet_text):
    analysis = TextBlob(tweet_text)
    sentiment_score = analysis.sentiment.polarity
    
    if sentiment_score > 0:
        return 'positivo'
    
    elif sentiment_score < 0:
        return 'negativo'
    
    else:
        return 'neutro'

## Matriz de correlacao
def matiz_corr(data):
    
    # Matriz
    matriz_corr = data.corr()
    plt.figure(figsize = (8, 6))
    sns.heatmap(matriz_corr, annot = True, 
                cmap = 'coolwarm', vmin = -1, vmax = 1)
    
    # Salvando
    plt.title('Matriz de Correlacao')
    plt.savefig(diretorio + '/correlacao_' + nameBD + '.png', 
                dpi = 300, bbox_inches = 'tight')

## Grafico de barras
def grafico_barras(data):
    
    # Espacamento e index
    bar_width = 0.2
    index = np.arange(len(data['Id_Date']))

    # Tamanho do grafico
    plt.figure(figsize=(12, 6))

    plt.bar(index - bar_width, data['Positivo'], bar_width, 
            label = 'Positivo', color = 'b', alpha = 0.7)
    plt.bar(index - bar_width, data['Negativo'], bar_width, 
            label = 'Negativo', color = 'r', alpha = 0.7)

    # Orientacao vertical
    plt.xticks(index, data['Id_Date'], rotation = 'vertical')

    # Posicao legenda y1
    plt.legend(loc = 'upper left')

    # Legenda y1
    plt.ylabel('Quantidade de Mencoes')

    # Criando eixo y2
    ax2 = plt.twinx()

    # Retorno no y2
    ax2.plot(index + bar_width, data['Retorno'], 
             marker = 'o', color = '.50', label = 'Retorno')

    # Posicao legenda y2
    ax2.legend(loc = 'upper right')

    # Legenda y2
    ax2.set_ylabel('Retorno (%)')

    # Titulo
    plt.title('Analise ' + nameBD)
    plt.grid(True)

    # Salvando
    plt.savefig(diretorio + '/analise_' + nameBD + '.png', 
                dpi = 300, bbox_inches = 'tight')

    plt.show()