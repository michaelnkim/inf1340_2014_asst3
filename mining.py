#!/usr/bin/env python3

"""
A Python Program that performs data mining on stock data,
which reads Stock Json file and calculates average prices of a stock, and returns the 6 best and worst months.
"""


# imports one per line
import json
import datetime




def read_stock_data(stock_name, stock_file_name):
    """
    Reads stock data JSON file, and creates list of tupules containing average and month.

    :param stock_name:String
    :param stock_file_name:String
    :return:List of Tupules
    """

    month = ""
    stock_data = []
    monthly_averages = []
    list_stock = read_json_from_file(stock_file_name)

    for stock in (list_stock):
        date_value = stock.get("Date")
        if date_value[0:7] == month:
            stock_data.append(stock)
        #Adds individual stock data if the data is within the same month as previous data.
        elif not stock_data:
            month = date_value[0:7]
            stock_data.append(stock)
       #For the first process when list stock_data is empty.
        else:
            monthly_averages.append(average_calculation(stock_data))
            stock_data = []
            month = date_value[0:7]
            stock_data.append(stock)
        #Calculate the monthly average, clear the list, and start the process again for different month.

    return monthly_averages


def six_best_months(list_tupules):
    """
    Sorts the list of tupules by the descending order of average stock price.
    :param list_tupules: List of tupules that contain month and average stock price.
    :return:Tupules. Six best month in sorted order from the entire list.
    """
    sorted_list = sorted(list_tupules, key= lambda average: average[1], reverse= True)

    return sorted_list[0:6]


def six_worst_months(list_tupules):
    """
    Sorts the list of tupules by the ascending order of average stock price.
    :param list_tupules: List of tupules that contain month and average stock price.
    :return:Tupules. Six worst month in sorted order from the entire list.
    """
    sorted_list = sorted(list_tupules, key= lambda average: average[1])

    return sorted_list[0:6]

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
        #Using for loop adds all the daily values to total values.

    average_calculated = total_sale / total_volume
    average_rounded = round(average_calculated, 2)
    #Rounded to 2 decimal places matching the test_mining case.
    date_month = stocklist[0].get("Date")
    average_month = (date_month[0:7], average_rounded)

    return average_month

def read_json_from_file(file_name):
    #Given Function that reads JSON file
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


print(six_best_months(read_stock_data("TSE-SO", "data/TSE-SO.json")))
print(six_worst_months(read_stock_data("TSE-SO", "data/TSE-SO.json")))

