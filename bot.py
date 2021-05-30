from logging import Logger
import websocket, json, pprint, talib, numpy

websocket.enableTrace(True)

SOCKET = "wss://stream.binance.com:9443/ws/adausdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

TRADE_SYMBOL = 'ADAUSDT'
TRADE_QUANTITY = 10

closes = []

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

    in_position = false

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
                else:
                    print("Overbought but you dont own anything")

            if last_rsi < RSI_OVERSOLD:

                if in_position:
                    print("It is oversold but you already own it, nothing to do")
                else:
                    print("BUYYYYY!!!!")

    # pprint.pprint(json_message)

print("starting connection")
try:
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
except:
    print("error")

