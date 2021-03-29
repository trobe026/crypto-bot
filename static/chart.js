const chart = LightweightCharts.createChart(document.getElementById('chart'), { width: 400, height: 300 });

const candleSeries = chart.addCandlestickSeries({
    upColor: '#00FF00',
    downColor: '#FF0000',
    borderDownColor:'#800080',
    borderUpColor:'#add8e6',
    wickDownColor: '#ffcccb',
    wickUpColor: '#90ee90'
});

fetch('http://localhost:5000/history')
    .then((r) => r.json())
    .then((response) => {
        console.log(response)
    });