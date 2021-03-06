import config, csv
from flask import Flask, render_template, request, flash, redirect, jsonify, session
from flask_cors import CORS, cross_origin
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = 'iowjaeionvneioa390IOJIOEV(@&OIJe' # secret key required for flask
client = Client(config.API_KEY, config.API_SECRET, tld='us')

@app.route('/')
def index():
    info = client.get_account()

    print(info)

    title = "CoinView"
    balances = info['balances']
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title=title, my_balances=balances, exchange=exchange_info, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    try:
        # print(request.form)

        order = client.create_order(
            symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity']
            )
            
    except Exception as e:
        # e.message no longer exists, simply convert entire message to string (figure how to get value by key eventually)
        flash(str(e), "error")

    return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
@cross_origin()
def history():
    candlesticks = client.get_historical_klines("ADAUSD", Client.KLINE_INTERVAL_5MINUTE, "1 day ago UTC")
    #candlesticks = client.get_historical_klines("ADAUSD", Client.KLINE_INTERVAL_15MINUTE, "1 May, 2021", "15 May, 2021")
    processed_candlesticks = []

    for data in candlesticks:

        candlestick = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        }

        processed_candlesticks.append(candlestick)
    
    return jsonify(processed_candlesticks)