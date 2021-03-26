import config, csv
from flask import Flask, render_template, request, flash, redirect, jsonify
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = 'iowjaeionvneioa390IOJIOEV(@&OIJe'
client = Client(config.API_KEY, config.API_SECRET, tld='us')

@app.route('/')
def index():
    info = client.get_account()

    title = "CoinView"
    balances = info['balances']
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']

    return render_template('index.html', title = title, my_balances=balances, exchange=exchange_info, symbols=symbols)

@app.route('/buy', methods=['POST'])
def buy():
    try:
        print(request.form)

        order = client.create_order(
            symbol=request.form['symbol'], 
            side=SIDE_BUY,
            type=ORDER_TYPE_MARKET,
            quantity=request.form['quantity']
            )
    except Exception as e:
        flash(str(e), "error")

    return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'