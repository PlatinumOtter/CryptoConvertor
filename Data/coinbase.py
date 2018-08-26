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


def update_coin(coin):
    try:
        connection = sqlite3.connect("exchanges.db")
        cursor = connection.cursor()
        rate = get_usd_exchange_rate(coin)
        date = datetime.datetime.now()
        sql_update = """
        UPDATE coinbase
        SET rate={money}, updated='{now}'
        WHERE coin='{abr}';
        """.format(money=rate, now=date, abr=coin)
        cursor.execute(sql_update)
        connection.commit()
    except:
        print("{abr} not updated for coinbase.".format(abr=coin))
    connection.close()


def update_all():
    coins = get_coin_list()
    for coin in coins:
        update_coin(coin)
