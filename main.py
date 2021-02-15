from urllib.request import urlopen
import json
import pandas as pd
import PySimpleGUI as sg
from testfile import invoke_rest_method
from openpyxl import Workbook


def get_stock_data(ticker):
    my_api_key = '6422462b31d8e0f20fc5841e1b8a6323'
    url = "https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=" + my_api_key
    df = invoke_rest_method(url)

    return df


def build_window_layout():
    sg.theme('DarkAmber')  # Add a touch of color
    layout = [
        [sg.Text('Ticker'), sg.InputText()],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    window = sg.Window("Main", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        if event == 'Ok' and len(values[0]) < 1:
            print('Please enter a valid ticker')
            break
        try:
            df = get_stock_data(values[0])
            build_table_from_dataframe(df)
            print('You entered ', values[0])
        except:
            print('Error finding ticker')

    window.close()


def build_table_from_dataframe(df, columnCSV=''):
    sg.set_options(auto_size_buttons=True)

    if len(columnCSV) > 1:
        commas = columnCSV.count(',')
        if commas > 0:
            column_list = columnCSV.split(',')
            data = df[column_list].values.tolist()
            header_list = df[column_list].columns.tolist()
        else:
            data = df[[columnCSV]].values.tolist()
            header_list = df[[columnCSV]].columns.tolist()
    else:
        data = df.values.tolist()
        header_list = df.columns.tolist()

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()
    window.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    build_window_layout()
    df = get_stock_data('MSFT')
    df.to_excel(f'C:/Users/carlos vega/pycharmprojects/FinancialVBA/test.xlsx')
    wb = Workbook()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
