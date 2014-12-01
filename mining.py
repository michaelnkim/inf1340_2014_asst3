#!/usr/bin/env python3

"""
A Python Program that performs data mining on stock data,
which reads Stock Json file and calculates avereage prices of a stock, and returns the 6 best and worst months.
"""


# imports one per line
import json
import datetime

stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """

    :param stock_name:
    :param stock_file_name:
    :return:
    """


    return



def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def organize_month(stock_file_name):
    """

    :param stock_file_name: List of Tupules
    :return:List of List of Tupules
    """
    xample = []
    month = ""
    for stock_data in (stock_file_name):
        date_value = stock_data.get("Date")
        test_list = []
        if date_value[0:7] == month:
            test_list.append(stock_data)
        else:
            #xample.append(calculate_average(test_list))
            test_list = []
            month = date_value[0:7]
        print (stock_data)
        print(xample)




"""def average_calcuation(list):
    ""

    :param list: list
    :return: value
    ""
    for stockdata_date in read_json_from_file(stock_file_name):
        volume_date = stockdata_date.get("Volume")
        close_date = stockdata_date.get("Close")
        totalsale_date = float(volume_date) * float(close_date)
"""


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

organize_month(read_json_from_file("data/GOOG.json"))

