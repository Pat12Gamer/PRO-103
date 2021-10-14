import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")

figure  = px.scatter(df, x="date", y="cases", color="country", size_max="20")

figure.show()