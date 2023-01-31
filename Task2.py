import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots #import new library

def top_platforms():
    df=pd.read_csv("vgsales.csv")

    #Grouping the north america sales based on each platform
    data2 = pd.DataFrame(df.groupby("Platform")[["NA_Sales"]].sum().sort_values(by=['NA_Sales'],ascending=[False]).reset_index())
    data2.rename(columns = {'Platform':'Platform_NA'}, inplace = True)

    #Grouping the europe sales based on each platform
    data3 = pd.DataFrame(df.groupby("Platform")[["EU_Sales"]].sum().sort_values(by=['EU_Sales'],ascending=[False]).reset_index())
    data3.rename(columns = {'Platform':'Platform_EU'}, inplace = True)

    #Grouping the japan sales based on each platform
    data4 = pd.DataFrame(df.groupby("Platform")[["JP_Sales"]].sum().sort_values(by=['JP_Sales'],ascending=[False]).reset_index())
    data4.rename(columns = {'Platform':'Platform_JP'}, inplace = True)

    #Grouping the other region sales based on each platform
    data5 = pd.DataFrame(df.groupby("Platform")[["Other_Sales"]].sum().sort_values(by=['Other_Sales'],ascending=[False]).reset_index())
    data5.rename(columns = {'Platform':'Platform_other'}, inplace = True)

    #Concatenating our datasets
    data=pd.concat([data2,data3,data4,data5],axis=1)
    data.head(3)



    subplot1 = make_subplots(rows=4, cols=1, shared_yaxes=True,subplot_titles=("North American top platforms","Europe top platforms","Japan top platforms","Other regions top platforms"))

    #Subplot for North America
    subplot1.add_trace(go.Bar(x=data['Platform_NA'], y=data['NA_Sales'],
                        marker=dict(color=[1, 2, 3],coloraxis="coloraxis")),1, 1)

    #Subplot for Europe
    subplot1.add_trace(go.Bar(x=data['Platform_EU'], y=data['EU_Sales'],
                        marker=dict(color=[4, 5, 6], coloraxis="coloraxis")),                         2, 1)
                    
    #Subplot for Japan
    subplot1.add_trace(go.Bar(x=data['Platform_JP'], y=data['JP_Sales'],
                        marker=dict(color=[7, 8, 9], coloraxis="coloraxis")),
                        3, 1)

    ##Subplot for Other Regions
    subplot1.add_trace(go.Bar(x=data['Platform_other'], y=data['Other_Sales'],
                        marker=dict(color=[10, 11, 12], coloraxis="coloraxis")),
                    4, 1)
                    
    subplot1.update_layout(height=900,width=500,coloraxis=dict(colorscale='Magenta'), showlegend=False)
    subplot1.show()