import plotly.graph_objects as go
import pandas as pd

data= pd.read_csv("/Users/Angus/Library/Mobile Documents/com~apple~CloudDocs/Work/Documents/i-SNAP project/Final library/Final sdf files/Combined libraries/Prop/Prop.csv")

fig = go.Figure(data=go.Scatter(x=data['MolWt'],
                                y=data['cLogP'],
                                mode='markers',
                                marker_color=data['Fsp3'],
                                text=data['Fsp3'])) # hover text goes here

fig.update_layout(title='MolWt vs cLogP vs Fsp3')
fig.show()
