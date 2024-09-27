import config

from alpaca.data.live.stock import StockDataStream

stock_data_stream_client = StockDataStream(config.API_KEY, config.SECRET_KEY, url_override = None)

async def stock_data_stream_handler(data):
    print(data)

symbol = 'AAPL'
symbols = [symbol]

stock_data_stream_client.subscribe_quotes(stock_data_stream_handler, *symbols) 
stock_data_stream_client.subscribe_trades(stock_data_stream_handler, *symbols)

stock_data_stream_client.run()