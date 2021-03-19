import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

# get all symbol prices
# prices = client.get_all_tickers()

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('15_min.csv', 'w', newline='')

candlestick_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for candle in candles:
    candlestick_writer.writerow(candle)
    # print(candle)


print(len(candles))