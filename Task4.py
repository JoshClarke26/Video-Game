import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots #import new library

def top_games_region():
    df=pd.read_csv("vgsales.csv")

    name2 = pd.DataFrame(df.groupby("Name")[["NA_Sales"]].mean().sort_values(by=['NA_Sales'],ascending=[False]).reset_index())
    name2.rename(columns = {'Name':'Name_NA'}, inplace = True)

    name3 = pd.DataFrame(df.groupby("Name")[["EU_Sales"]].mean().sort_values(by=['EU_Sales'],ascending=[False]).reset_index())
    name3.rename(columns = {'Name':'Name_EU'}, inplace = True)

    name4 = pd.DataFrame(df.groupby("Name")[["JP_Sales"]].mean().sort_values(by=['JP_Sales'],ascending=[False]).reset_index())
    name4.rename(columns = {'Name':'Name_JP'}, inplace = True)

    name5 = pd.DataFrame(df.groupby("Name")[["Other_Sales"]].mean().sort_values(by=['Other_Sales'],ascending=[False]).reset_index())
    name5.rename(columns = {'Name':'Name_other'}, inplace = True)

    #Concatenating the results.
    name_df=pd.concat([name2,name3,name4,name5],axis=1)

    subplot_name1 = make_subplots(rows=4, cols=1, shared_yaxes=True,subplot_titles=("North American top games","Europe top games", "Japan top games","Other regions top games",'Top games globally'))

    #Subplot for North America
    subplot_name1.add_trace(go.Bar(x=name_df['Name_NA'][:5], y=name_df['NA_Sales'][:5],marker=dict(color=[1, 2, 3],coloraxis="coloraxis")),1, 1)

    #Subplot for Europe
    subplot_name1.add_trace(go.Bar(x=name_df['Name_EU'][:5], y=name_df['EU_Sales'][:5],marker=dict(color=[4, 5, 6], coloraxis="coloraxis")), 2, 1)

    #Subplot for Japan
    subplot_name1.add_trace(go.Bar(x=name_df['Name_JP'][:5], y=name_df['JP_Sales'][:5],marker=dict(color=[7, 8, 9], coloraxis="coloraxis")),3, 1)

    #Subplot for other regions
    subplot_name1.add_trace(go.Bar(x=name_df['Name_other'][:5], y=name_df['Other_Sales'][:5],marker=dict(color=[10, 11, 12], coloraxis="coloraxis")),4, 1)

    subplot_name1.update_layout(height=1000,width=500,coloraxis=dict(colorscale='Mint_r'), showlegend=False)
    subplot_name1.update_xaxes(tickangle=45)
    subplot_name1.show()