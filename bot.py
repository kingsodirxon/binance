import pandas as pd

apiKey = '7Z5R5PTNGVS0GUSB'

interval_var = '5min'
symbol = 'ETH'

path = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol='+symbol + \
    '&market=USD&interval='+interval_var+'&apikey=' + \
    apiKey+'&datatype=csv&outputsize=full'

df = pd.read_csv(path)

df = df[::-1].reset_index()

df = df.drop(['index'], axis=1)
