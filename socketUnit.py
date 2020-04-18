import websocket
from threading import Thread
import time
import sys, json
import pymysql
from config import *


def run_query(db, query):
    """
    Execute Query in mysql
    :param db: db connection
    :param query: string
    :return: array
    """
    data = []
    json_data = []
    cursor = db.cursor()
    try:
        cursor.execute(query)
        db.commit()
        row_headers = [x[0] for x in cursor.description]
        data = cursor.fetchall()
        for result in data:
            json_data.append(dict(zip(row_headers, result)))
        cursor.close()
    except Exception as e:
        db.rollback()
        # print("Sql statement Error!")
    cursor.close()
    return data, json_data

class SocketUnit():

    def get_value(self, arr, name):
        """
        Reterieve value by name from array
        :param arr: array
        :param name: string
        :return: Mixed
        """
        if name in arr:
            return arr[name]
        return ''

    def on_message(self, ws, message):
        """
        On Message function of Websocket
        :param ws: websocket instance
        :param message: string
        :return: None
        """
        data = json.loads(message)
        db = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

        if 'data' in data:
            for row in data['data']:
                orderID = self.get_value(row, 'orderID')
                symbol = self.get_value(row, 'symbol')
                side = self.get_value(row, 'side')
                price = self.get_value(row, 'price')
                price = 0 if price == '' else price
                leavesQty = self.get_value(row, 'leavesQty')
                leavesQty = 0 if leavesQty == '' else leavesQty
                action = self.get_value(data, 'action')

                query = "insert into liquidations (action, orderid, symbol, side, price, leavesQty) values ('%s','%s', '%s', '%s', %s, %s)" % (
                action, orderID, symbol, side, price, leavesQty)
                run_query(db, query)
                print(data)

    def on_error(self, ws, error):
        print(error)


    def on_close(self, ws):
        print("### closed ###")


    def on_open(self, ws):
        def run(*args):
            while True:
                time.sleep(1)
            ws.close()
            print("Thread terminating...")
        Thread(target=run).start()


    def run(self):
        """
        Socket Run Forever
        :return: None
        """
        websocket.enableTrace(True)
        host = "wss://testnet.bitmex.com/realtime?subscribe=liquidation:"
        ws = websocket.WebSocketApp(host,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

