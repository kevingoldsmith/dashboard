# -*- coding: utf-8 -*-
import plotly.graph_objects as go
import csv
import os
import datetime
import dateutil.parser

DATA_DIR = '../data/twitter'
DATA_FILE = 'new_follower_count.csv'

data_path = os.path.join(DATA_DIR, DATA_FILE)
results = []

with open(data_path) as csvfile:
    csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in csvreader:
        results.append(row)

x = []
y = []
plus = []
minus = []

for res in results[-50:]:
    x.append(dateutil.parser.parse(res[0]))
    y.append(res[1])
    plus.append(res[2])
    minus.append(res[3])

fig = go.Figure(data=go.Scatter(
        x=x,
        y=y,
        error_y=dict(
            type='data',
            symmetric=False,
            array=plus,
            arrayminus=minus)
        ))
fig.show()
