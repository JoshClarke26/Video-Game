import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def highest_sales():
    df=pd.read_csv("vgsales.csv")

    x=(df['NA_Sales'].mean()*1000000)
    y=(df['EU_Sales'].mean()*1000000)
    z=(df['JP_Sales'].mean()*1000000)
    q=(df['Other_Sales'].mean()*1000000)
    p=(df['Global_Sales'].mean()*1000000)

    print("The average sales in North America =", (f"${x:,.3f}")) #comma separated values till 3 decimal place and $ sign
    print("The average sales in Europe =",(f"${y:,.3f}"))
    print("The average sales in Japan =",(f"${z:,.3f}"))
    print("The average sales in other regions =",(f"${q:,.3f}"))
    print("The average sales globally =",(f"${p:,.3f}"))

    colors = ['lightslategray',] * 4
    colors[1]='darkgray'
    colors[2]='grey'
    colors[3]='dimgrey'
    colors[0] = 'crimson'

    bar1 = go.Figure(data=[go.Bar(
        y=['Global','North America', 'Europe', 'Japan',
        'Other'],
        x=[537440.656,264667.430, 146652.006, 77781.660, 48063.020],
        orientation='h',
        marker_color=colors # marker color can be a single color value or an iterable
    )])
    bar1.update_layout(title_text='Region with highest sales on an average')
    bar1.update_xaxes(title='Average Sales')
    bar1.update_yaxes(title='Regions')
    bar1.show()