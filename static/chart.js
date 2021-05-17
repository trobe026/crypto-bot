
// const fetch = require('node-fetch');

// eslint-disable-next-line no-undef
const chart = LightweightCharts.createChart(document.getElementById('chart'), { width: 750, height: 420 });

const candleSeries = chart.addCandlestickSeries({
    upColor: '#00FF00',
    downColor: '#FF0000',
    borderDownColor:'#800080',
    borderUpColor:'#add8e6',
    wickDownColor: '#ffcccb',
    wickUpColor: '#90ee90'
});

// eslint-disable-next-line no-undef
fetch('http://localhost:5000/history')
    .then((r) => r.json())
    .then((response) => {
        candleSeries.setData(response);
    });


// var binanceSocket = new WebSocket("wss://stream.binance.com:9443:ws/btcusdt@kline_15m");
// binanceSocket.onmessage = function(event) {
//     console.log(event.data)
// }