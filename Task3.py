import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots #import new library

def top_10():
    df=pd.read_csv("vgsales.csv")

    top = pd.DataFrame(df.groupby("Name")[["Global_Sales"]].sum().sort_values(by=['Global_Sales'],ascending=[False]).reset_index())
    top.head(10) #Printing the top 10 results

    pie1 = px.pie(top, values=top['Global_Sales'][:10], names=top['Name'][:10],title='Top 10 games globally', 
                color_discrete_sequence=px.colors.sequential.Purp_r)
    pie1.update_traces(textposition='inside', textinfo='percent+label',showlegend=False)

    pie1.show()