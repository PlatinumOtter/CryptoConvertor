import datetime
import os
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/<string:table>', methods=['GET'])
def getrate(table):
    coin = "{}".format(request.args.get('coin'))
    if table != 'coinbase' and coin == 'BTC':
        return jsonify({'rate': 1, 'updated': datetime.datetime.now()})
    else:
        connection = sqlite3.connect(os.path.join(os.pardir, "Data", "exchanges.db"))
        cursor = connection.cursor()
        query = 'select rate, updated from {thetable} where coin="{thecoin}";'.format(thetable=table, thecoin=coin)
        resp = cursor.execute(query).fetchall()
        connection.close()
        return jsonify({'rate': resp[0][0], 'updated': resp[0][1]})


@app.route('/api/v1.0/listcoins/<string:table>', methods=['GET'])
def getcoinlist(table):
    connection = sqlite3.connect(os.path.join(os.pardir, "Data", "exchanges.db"))
    cursor = connection.cursor()
    query = 'select coin from {};'.format(table)
    resp = cursor.execute(query).fetchall()
    connection.close()
    return jsonify({'coins': resp})

@app.route('/api/v1.0/convert/<string:table>', methods=['GET'])
def convert(table):
    coin1 = "{}".format(request.args.get('coin1'))
    coin2 = "{}".format(request.args.get('coin2'))
    amount = request.args.get('amount')
    connection = sqlite3.connect(os.path.join(os.pardir, "Data", "exchanges.db"))
    cursor = connection.cursor()
    query = 'select rate from {thetable} where coin="{thecoin}";'.format(thetable=table, thecoin=coin)


if __name__ == '__main__':
    app.run(debug=True)
