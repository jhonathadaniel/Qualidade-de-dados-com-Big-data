import tweepy

# Credenciais da API do Twitter
consumer_key = 'TZI5nS2SB5Lew0yOlI711C71H'
consumer_secret = 'VAcj1TVArWbgDDomHinxtju1pzqnPo5zwF8ZqItgtfaLgF4em5'
access_token = '1764287314266558464-c4a0WDIXxukkHetJFIbzTJoqHhmpV9'
access_token_secret = 'ZQvr6b170oHdvXUIWx4NBV2S3mGRNOfthWIkGdnmCbOPC'

# Autenticação
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Palavras-chave para pesquisa
palavras_chave = ['python', 'machine learning', 'data science']

# Coletar tweets
tweets_coletados = []
for palavra in palavras_chave:
    resultados = api.search_tweets(q=palavra, count=10)  # Coleta 10 tweets para cada palavra-chave
    for tweet in resultados:
        tweets_coletados.append(tweet.text)

# Exibir os tweets coletados
for i, tweet in enumerate(tweets_coletados, start=1):
    print(f'Tweet {i}: {tweet}')
