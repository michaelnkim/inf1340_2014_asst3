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
    xample = []
    month = ""
    list_stock_data = read_json_from_file(stock_file_name)
    test_list = []
    for stock_data in (list_stock_data):
        date_value = stock_data.get("Date")
        if date_value[0:7] == month:
            test_list.append(stock_data)
            print("append")
        elif not test_list:
            month = date_value[0:7]
            test_list.append(stock_data)
            print("begining")
        else:
            xample.append(average_calculation(test_list))
            test_list = []
            month = date_value[0:7]
            test_list.append(stock_data)
            print("vds")
    return xample


def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def average_calculation(stocklist):
    """
    Function that calculates the average of stock sales per months
    :param stocklist: list that contains stock data list
    :return: tupule with average calculated and month
    """
    total_volume = 0.0
    total_sale = 0.0
    for stockdata in stocklist:
        volume_date = stockdata.get("Volume")
        close_date = stockdata.get("Close")
        total_sale_date = float(volume_date) * float(close_date)
        total_volume += volume_date
        total_sale += total_sale_date
    average_calculated = total_sale / total_volume
    date_month = stocklist[0].get("Date")
    average_month = (average_calculated, date_month[0:7])
    return average_month

def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


print(read_stock_data("GOOG", "data/GOOG.json"))

