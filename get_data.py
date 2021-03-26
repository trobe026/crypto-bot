import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# get all symbol prices
# prices = client.get_all_tickers()

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# fetch 30 minute klines for the last month of 2017
candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2017", "1 Jan, 2021")

# csvfile = open('15_min.csv', 'w', newline='')
csvfile = open('2017-2021.csv', 'w', newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for candle in candles:
    candlestick_writer.writerow(candle)
    # print(candle)


print(len(candles))