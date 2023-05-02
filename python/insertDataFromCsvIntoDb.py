"""
    Retreive signal API
    author: Noureddine AYAD
    date=27 april 2023 
"""
import mysql.connector
from signalsProcessing import getSignals


def insertDataFromCsvToDb(signalsFileFullPath, keywordsFileFullPath):

    try:
        """ connection = mysql.connector.connect(host='localhost',
                                             database='signals_db',
                                             user='root',
                                             password='Mysql-1310') """
        connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port="3306", database='signals_db')

        query = f"INSERT INTO signals VALUES (%s, %s, %s, %s, %s, %s)"
        rows = getDataListFromCsvFile(
            signalsFileFullPath, keywordsFileFullPath)
        cursor = connection.cursor()
        cursor.executemany(query, rows)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def getDataListFromCsvFile(signalsFileFullPath, keywordsFileFullPath):

    signals = getSignals(signalsFileFullPath, keywordsFileFullPath)
    rows = []
    if signals:
        for key in signals.keys():
            node_id = key
            sampling_interval_ms = int(signals[node_id]["sampling_interval_ms"]) if (type(
                signals[node_id]["sampling_interval_ms"]) == str and signals[node_id]["sampling_interval_ms"] != '') else 0

            deadband_value = int(signals[node_id]["deadband_value"]) if (type(
                signals[node_id]["deadband_value"]) == str and signals[node_id]["deadband_value"] != '') else 0

            deadband_type = signals[node_id]["deadband_type"] if (
                signals[node_id]["deadband_type"] != '') else ''

            active = int(signals[node_id]["active"]) if (type(signals[node_id]["active"]) == str and
                                                         signals[node_id]["active"] != '') else 0

            keywords = ';'.join(signals[node_id]["keywords"]) if (type(
                signals[node_id]["keywords"]) == list and signals[node_id]["keywords"] != '') else ''

            rowTuple = (node_id, sampling_interval_ms,
                        deadband_value, deadband_type, active, keywords)
            rows.append(rowTuple)
    return rows


def printSignals():
    try:
        """ connection = mysql.connector.connect(host='localhost',
                                             database='signals_db',
                                             user='root',
                                             password='Mysql-1310') """
        connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port="3306", database='signals_db')
        query = """SELECT * FROM signals"""

        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3], row[4])

    except mysql.connector.Error as error:
            print("Failed to get data from table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



