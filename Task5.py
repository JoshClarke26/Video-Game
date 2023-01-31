import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots #import new library
import numpy as np #import library

def genre_global_sales():

    df=pd.read_csv("vgsales.csv")

    old_games = pd.DataFrame(df.query('Year<2000', inplace=False))

    old_games.query('Global_Sales>7.8235', inplace=False)
    genre_df = df.groupby("Genre")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index()
    genre_df #print the dataframe
    bar_genre= px.bar(genre_df, x='Genre', y='Global_Sales',color='Global_Sales',color_continuous_scale='Burgyl')
    bar_genre.show()