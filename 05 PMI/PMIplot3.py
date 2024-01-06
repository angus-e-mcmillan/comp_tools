import plotly.express as pd
data= pd.read_csv("/Users/Angus/Library/Mobile Documents/com~apple~CloudDocs/Work/Documents/i-SNAP project/Final library/Final sdf files/Combined libraries/PMI/PMI data.csv")

fig = pd.scatter(df, x=data["PMI1"], y=data["PMI2"], color=data["PBF"],
                 title="test")

fig.show()
