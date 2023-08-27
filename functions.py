## [--DataBase--] ##

## Importacoes
import pandas as pd
import yfinance as yf
from textblob import TextBlob

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