import pandas as pd
import csv
import plotly.graph_objects as go

Df = pd.read_csv("Data.csv")
studentDf = Df.loc[Df['student_id'] == "TRL_987"]
print(studentDf.groupby("level")["attempt"].mean())
fig = go.Figure(go.Bar(
    x = Df.groupby("level")["attempt"].mean(),
    y = ['Level 1','Level 2','Level 3','Level 4'],
    orientation = 'h'
))
fig.show()