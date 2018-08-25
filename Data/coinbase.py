import sqlite3
import requests
import json
import datetime

coinbase_coins = ["BTC", "BCH", "ETH", "LTC"]


def get_usd_exchange_rate(coin):
    resp = requests.get(
        "https://api.coinbase.com/v2/prices/{abr}-USD/spot"
        .format(abr=coin))
    if resp.status_code == 200:
        return json.loads(resp.text)["data"]["amount"]
    else:
        ValueError("Non 200 response from server")
    resp.close()


def get_coin_list():
    return coinbase_coins


def update_coinbase():
    connection = sqlite3.connect("exchanges.db")
    cursor = connection.cursor()
    coins=get_coin_list()
    for coin in coins:
        try:
            rate = get_usd_exchange_rate(coin)
            date = datetime.datetime.now()
            sql_update = """
            UPDATE coinbase
            SET usd={money}, updated='{now}'
            WHERE coin='{abr}';
            """.format(money=rate, now=date, abr=coin)
            cursor.execute(sql_update)
        except:
            print("{abr} not updated.".format(abr=coin))
    connection.commit()
    connection.close()


update_coinbase()
