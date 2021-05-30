import backtrader as bt

class RSIStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 60 and not self.position:
            self.buy(size=100)


        if self.rsi > 85 and self.position:
            self.close()


cerebro = bt.Cerebro()


data = bt.feeds.GenericCSVData(dataname='ada_2021_may_5min.csv', dtformat=2, compression=5, timeframe=bt.TimeFrame.Minutes)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()