import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# get all symbol prices
# prices = client.get_all_tickers()

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('ada_2021_may_5min.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

# fetch 1 day klines from beginning 2021 to current
# candlesticks = client.get_historical_klines("ADAUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "22 May, 2021")
candlesticks = client.get_historical_klines("ADAUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 May, 2021")
print(len(candlesticks))

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close();    