import sqlite3

connection = sqlite3.connect("exchanges.db")
cursor = connection.cursor()

# Coinbase table setup

drop_coinbase = "DROP TABLE IF EXISTS coinbase"
cursor.execute(drop_coinbase)

create_coinbase_table = """
CREATE TABLE coinbase (
coin VARCHAR(10) PRIMARY KEY,
usd FLOAT DEFAULT 1,
updated DATETIME DEFAULT 0);"""
cursor.execute(create_coinbase_table)

coinbase_coins = ["BTC", "BCH", "ETH", "LTC"]

for coin in coinbase_coins:
    add_coin = """
    INSERT INTO coinbase (coin)
    VALUES ("{coinabbr}")""".format(coinabbr=coin)
    print(add_coin)
    cursor.execute(add_coin)

connection.commit()

# Binance table setup

drop_binance = "DROP TABLE IF EXISTS binance"
cursor.execute(drop_binance)

create_binance_table = """
CREATE TABLE binance (
coin VARCHAR(10) PRIMARY KEY,
btc FLOAT DEFAULT 1,
updated DATETIME DEFAULT 0);"""
cursor.execute(create_binance_table)

binance_coins = ["LTC", "ETH", "ZEC", "DASH", "XRP", "XMR"]

for coin in binance_coins:
    add_coin = """
    INSERT INTO binance (coin)
    VALUES ("{coinabbr}")""".format(coinabbr=coin)
    print(add_coin)
    cursor.execute(add_coin)

connection.commit()

connection.close()
