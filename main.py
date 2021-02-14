# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from urllib.request import urlopen
import json
import pandas as pd
import PySimpleGUI as sg


def get_stockprice(ticker):
    myapikey = '6422462b31d8e0f20fc5841e1b8a6323'
    url = "https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=" + myapikey
    response = urlopen(url)
    urldata = response.read().decode("utf-8")
    my_json = json.loads(urldata)
    pd1 = pd.DataFrame(my_json)
    stockprice = pd1["price"].values[0]
    return stockprice


def build_window_layout():
    sg.theme('DarkAmber')  # Add a touch of color
    layout = [
        [sg.Text('Ticker'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    window = sg.Window("mainss", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        stock_price = get_stockprice(values[0])
        stock_price2 = table_example(values[0])
        print('You entered ', values[0], stock_price)

    window.close()


def table_example(ticker):
    sg.set_options(auto_size_buttons=True)
    # Header=None means you directly pass the columns names to the dataframe
    myapikey = '6422462b31d8e0f20fc5841e1b8a6323'
    url = "https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=" + myapikey
    response = urlopen(url)
    urldata = response.read().decode("utf-8")
    my_json = json.loads(urldata)
    df = pd.DataFrame(my_json)
    data = df[["symbol", "price"]].values.tolist()  # read everything else into a list of rows
    # Uses the first row (which should be column names) as columns names
    print(df[["symbol", "price"]].values.tolist())
    header_list = df[["symbol", "price"]].columns.tolist()
    # Drops the first row in the table (otherwise the header names and the first row will be the same)



    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()
    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    build_window_layout()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
