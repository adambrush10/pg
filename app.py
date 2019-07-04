from flask import Flask, render_template, request, url_for, flash, redirect, send_file, Response
import requests
import pandas as pd
import numpy as np
from yahoofinancials import YahooFinancials
import json
import requests
from datetime import datetime, date
from flask_wtf import FlaskForm
from wtforms import StringField
#from form import InputForm
from wtforms.validators import InputRequired


app = Flask(__name__)

app.config['SECRET_KEY']='1010'

class PriceForm(FlaskForm):
    symbol = StringField('ticker', validators=[InputRequired()])
    start = StringField('startdate', validators=[InputRequired()])
    end = StringField('enddate', validators=[InputRequired()])

@app.route('/', methods=['GET', 'POST'])

def submitted():

    form = PriceForm()
    if form.validate_on_submit():
        format_str = '%Y-%m-%d'
        symbol = form.symbol.data
        print(symbol)
        start = form.start.data
        start = datetime.strptime(start, format_str).strftime(format_str)
        print(start)
        end= form.end.data
        end= datetime.strptime(end, format_str).strftime(format_str)
        print(end)
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


        close = []
        x = 0
        while x < Y:
            dai = m_data[symbol]['prices'][x]['close']
            close.append(dai)
            x +=1


        volume = []
        x = 0
        while x < Y:
            dai = m_data[symbol]['prices'][x]['volume']
            volume.append(dai)
            x +=1


        final_output = pd.DataFrame(list(zip(dates, high, low, opens, close, volume)),
                     columns=['date','high', 'low', 'open', 'close', 'volume'])

        final_csv = final_output.to_csv()
        print(final_csv)
        print('done')
        return Response(final_csv,mimetype="text/csv",headers={"Content-disposition":"attachment; filename=results.csv"})
    return render_template('index.html', form=form)

#else:
    #print('nah fam')
    #return 'nothing'
    #return final_output



    #print(f'the symbol is {symbol}, the start date is {start} and the end date is {end}')







if __name__ == '__main__':
    app.run(debug=True)
