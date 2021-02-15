from urllib.request import urlopen
import json
import pandas as pd


def invoke_rest_method(url):
    # Returns pandas dataframe from web request as formatted json
    response = urlopen(url)
    url_data = response.read().decode("utf-8")
    my_json = json.loads(url_data)
    df = pd.DataFrame(my_json)

    return df
