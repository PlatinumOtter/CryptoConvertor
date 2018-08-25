import sqlite3
import requests
import json
import datetime

bitfinex_coins = ["LTC", "ETH", "ZEC", "XRP", "XMR"]

def get_btc_exchange_rate(coin):
    resp = requests.get("https://api.bitfinex.com/v2/ticker/t{}BTC".format(coin))
    if resp.status_code == 200:
        return resp.text.split(",")[8]
    else:
        ValueError("Non 200 response from server")
    resp.close()


def get_coin_list():
    return bitfinex_coins


def update_bitfinex():
    connection = sqlite3.connect("exchanges.db")
    cursor = connection.cursor()
    coins = get_coin_list()
    for coin in coins:
        try:
            rate = get_btc_exchange_rate(coin)
            date = datetime.datetime.now()
            sql_update = """
            UPDATE bitfinex
            SET btc={money}, updated='{now}'
            WHERE coin='{abr}';
            """.format(money=rate, now=date, abr=coin)
            cursor.execute(sql_update)
            print(sql_update)
        except:
            print("{abr} not updated.".format(abr=coin))
    connection.commit()
    connection.close()
