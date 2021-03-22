import config, csv
from flask import Flask, render_template, request
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET, tld='us')

@app.route('/')
def index():
    title = "CoinView"
    info = client.get_account()
    balances = info['balances']
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    return render_template('index.html', title = title, my_balances=balances, exchange=exchange_info, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    order = client.create_order(symbol='ADAUSD', side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=100,
        price='0.00001')
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'