import pandas as pd
import csv
import plotly.express as go

Df = pd.read_csv("Data.csv")
mean = Df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
fig = go.scatter(mean,x = "student_id",y = "level",size = "attempt", color = "attempt")
fig.show()