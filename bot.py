from logging import Logger
import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *


# websocket.enableTrace(True)

data = [1.5874, 1.5775, 1.5689, 1.5683, 1.5649, 1.5655, 1.5697, 1.5696, 1.5713, 1.5684, 1.5608, 1.5694, 1.5647, 1.5595, 1.5686, 1.5675, 1.5716, 1.573, 1.5745, 1.5734, 1.5681, 1.5731, 1.5706, 1.5677, 1.5657, 1.5639, 1.5701]

SOCKET = "wss://stream.binance.com:9443/ws/adausdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

TRADE_SYMBOL = 'ADAUSDT'
TRADE_QUANTITY = 10

closes = []
in_position = False

client = Client(config.API_KEY, config.API_SECRET, tld='us')

def on_open(ws):
    print("ran")
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    print('received message')

    global closes

    json_message = json.loads(message)

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("rsi's calculated so far")
            print(rsi)

            last_rsi = rsi[-1]
            print("current rsi is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought and you own it, SELLL!!!")
                    in_position = False
                    # sell logic here
                else:
                    print("Overbought but you dont own anything")

            if last_rsi < RSI_OVERSOLD:

                if in_position:
                    print("It is oversold but you already own it, nothing to do")
                else:
                    # buy logic here
                    in_position = True
                    print("BUYYYYY!!!!")

    # pprint.pprint(json_message)

print("starting connection")
try:
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
except:
    print("error")

