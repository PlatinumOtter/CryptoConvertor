import sqlite3
import requests
import json
import datetime

binance_coins = ["LTC", "ETH", "ZEC", "DASH", "XRP", "XMR"]

def get_btc_exchange_rate(coin):
    resp = requests.get("https://api.binance.com/api/v3/ticker/price",
                        params={'symbol': '{abr}BTC'.format(abr=coin)})
    if resp.status_code == 200:
        return json.loads(resp.text)['price']
    else:
        ValueError("Non 200 response from server")
    resp.close()


def get_coin_list():
    return binance_coins


def update_binance():
    connection = sqlite3.connect("exchanges.db")
    cursor = connection.cursor()
    coins = get_coin_list()
    for coin in coins:
        try:
            rate = get_btc_exchange_rate(coin)
            date = datetime.datetime.now()
            sql_update = """
            UPDATE binance
            SET btc={money}, updated='{now}'
            WHERE coin='{abr}';
            """.format(money=rate, now=date, abr=coin)
            cursor.execute(sql_update)
        except:
            print("{abr} not updated.".format(abr=coin))
    connection.commit()
    connection.close()
