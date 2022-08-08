
import flask
from flask import request
import numpy as np
import pandas as pd


rss =[]
app = flask.Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def handle_request():
    rs = request.args.get('names')
    print(rs)
    rss.append(rs)
    return "hi"
app.run(host="0.0.0.0", port=777)

df = pd.DataFrame()
df['rssi'] = rss[0::1]
df.to_excel('rssi.xlsx', index = False)


import xlsxwriter
with xlsxwriter.Workbook('r.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(rss):
        worksheet.write_row(row_num, 0, data)
        
