import sqlite3
import coinbase
import binance
import bitfinex

connection = sqlite3.connect("exchanges.db")
cursor = connection.cursor()

# Coinbase table setup

drop_coinbase = "DROP TABLE IF EXISTS coinbase"
cursor.execute(drop_coinbase)

create_coinbase_table = """
CREATE TABLE coinbase (
coin VARCHAR(10) PRIMARY KEY,
rate FLOAT DEFAULT 1,
updated DATETIME DEFAULT 0);"""
cursor.execute(create_coinbase_table)

coinbase_coins = coinbase.get_coin_list()

for coin in coinbase_coins:
    add_coin = """
    INSERT INTO coinbase (coin)
    VALUES ("{abr}")""".format(abr=coin)
    cursor.execute(add_coin)

connection.commit()

# Binance table setup

drop_binance = "DROP TABLE IF EXISTS binance"
cursor.execute(drop_binance)

create_binance_table = """
CREATE TABLE binance (
coin VARCHAR(10) PRIMARY KEY,
rate FLOAT DEFAULT 1,
updated DATETIME DEFAULT 0);"""
cursor.execute(create_binance_table)

binance_coins = binance.get_coin_list()

for coin in binance_coins:
    add_coin = """
    INSERT INTO binance (coin)
    VALUES ("{abr}")""".format(abr=coin)
    cursor.execute(add_coin)

connection.commit()

# Bitfinex table setup

drop_bitfinex = "DROP TABLE IF EXISTS bitfinex"
cursor.execute(drop_bitfinex)

create_bitfinex_table = """
CREATE TABLE bitfinex (
coin VARCHAR(10) PRIMARY KEY,
rate FLOAT DEFAULT 1,
updated DATETIME DEFAULT 0);"""
cursor.execute(create_bitfinex_table)

bitfinex_coins = bitfinex.get_coin_list()

for coin in bitfinex_coins:
    add_coin = """
    INSERT INTO bitfinex (coin)
    VALUES ("{abr}")""".format(abr=coin)
    cursor.execute(add_coin)

connection.commit()

connection.close()
