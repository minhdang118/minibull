import sqlite3, config

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient(config.API_KEY, config.SECRET_KEY)

account = trading_client.get_account()
if account.trading_blocked:
    print('Account is currently restricted from trading.')
    
print('Account number: {}'.format(account.account_number))

print('${} is available as buying power.'.format(account.buying_power))

balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')