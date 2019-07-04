import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials
import json
import requests
from datetime import datetime, date, timedelta, time

def price_getter():
    symbol = 'AAPL'
    start = '2019-06-20'
    end = '2019-06-24'
    day = 'daily'

    yahoo_financials = YahooFinancials(symbol)
    m_data= yahoo_financials.get_historical_price_data(start, end, day)

    Y = len(m_data[symbol]['prices'])

    D_end = datetime.strptime(end, '%Y-%m-%d')
    D_start = datetime.strptime(start, '%Y-%m-%d')

    #create the lists
    dates = []
    x = 0
    while x < Y:
        dai = m_data[symbol]['prices'][x]['formatted_date']
        dates.append(dai)
        x +=1

    high = []
    x = 0
    while x < Y:
        dai = m_data[symbol]['prices'][x]['high']
        high.append(dai)
        x +=1

    low = []
    x = 0
    while x < Y:
        dai = m_data[symbol]['prices'][x]['low']
        low.append(dai)
        x +=1

    opens = []
    x = 0
    while x < Y:
        dai = m_data[symbol]['prices'][x]['open']
        opens.append(dai)
        x +=1
    print(opens)

    close = []
    x = 0
    while x < Y:
        dai = m_data[symbol]['prices'][x]['close']
        close.append(dai)
        x +=1
    print(close)

    volume = []
    x = 0
    while x < Y:
        dai = m_data[symbol]['prices'][x]['volume']
        volume.append(dai)
        x +=1
    print(volume)

    final_output = pd.DataFrame(list(zip(dates, high, low, opens, close, volume)),
                  columns=['date','high', 'low', 'open', 'close', 'volume'])

    final_csv = final_output.to_csv()

    return final_output
