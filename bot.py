import websocket
websocket._logging._logger.level = -99 # This will enable all levels of logging
websocket._logging.en(True)

SOCKET = "wss://stream.binance.com:9443/ws/adausdt@kline_1m"

def on_open():
    print("ran")
    print('opened connection')

def on_close():
    print('closed connection')

def on_message():
    print('received message')  

ws2 = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)

ws2.run_forever()
print("running")

# def on_open():
#     print("ran")
#     print('opened connection')

# def on_close():
#     print('closed connection')

# def on_message():
#     print('received message')        

# print("starting connection")
# try:
#     ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
#     ws.run_forever()
# except:
#     print("error")    


print("here")
print("finish")

