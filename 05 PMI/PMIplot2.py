import plotly.graph_objects as go
import pandas as pd

data= pd.read_csv("/Users/Angus/Library/Mobile Documents/com~apple~CloudDocs/Work/Documents/i-SNAP project/Final library/Final sdf files/Combined libraries/PMI/PMI data.csv")

fig = go.Figure(data=go.Scatter(x=data['PMI1'],
                                y=data['PMI2'],
                                mode='markers',
                                marker_color=data['PBF'],
                                text=data['PBF'])) # hover text goes here

fig.update_layout(title='PMI vs PBF')

fig.show()

