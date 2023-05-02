"""
    Signal processing  API
    author: Noureddine AYAD
    date=27 april 2023 
"""
import json
import mysql.connector
from fastapi import FastAPI


app = FastAPI(title="singalsAPI", version="v1")

# get all signal from db


@app.get("/")
async def getSignals():

    try:
        connection = mysql.connector.connect(
            user='root', password='root', host='mysql', port="3306", database='signals_db')
        cursor = connection.cursor()
        query = """ Select * from signals """
        cursor.execute(query)
        # get all signals
        rows = cursor.fetchall()
        signals = []
        for row in rows:
            signal = {}
            signal['node_id'] = row[0]
            signal['sampling_interval_ms'] = row[1]
            signal['deadband_value'] = row[2]
            signal['deadband_type'] = row[3]
            signal['active'] = row[4]
            signal['keywords'] = row[5]
            signals.append(signal)

    except mysql.connector.Error as error:
        print("Failed to get signal from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return json.dumps(signals, skipkeys=True,
                      allow_nan=True)


@app.get("/signals/{node_id}")
async def getSignal(node_id: str):
    signal = {}

    if (type(node_id) ==str  and node_id != ''):
        try:
            connection = mysql.connector.connect(
            user='root', password='root', host='mysql', port="3306", database='signals_db')
            cursor = connection.cursor()
            query = """ Select * FROM signals WHERE node_id= %s """
            # set variable in query
            cursor.execute(query, (node_id,))
            row = cursor.fetchall()
            signal['node_id'] = row[0][0]
            signal['sampling_interval_ms'] = row[0][1]
            signal['deadband_value'] = row[0][2]
            signal['deadband_type'] = row[0][3]
            signal['active'] = row[0][4]
            signal['keywords'] = row[0][5]

        except mysql.connector.Error as error:
            print("Failed to get signal from MySQL table {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

        return json.dumps(signal)

    else:
        return "node_id is not valid...!!!"



