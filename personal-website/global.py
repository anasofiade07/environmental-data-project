import plotly.express as px
import pandas as pd

# Sample data
data = {
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Lat': [40.7128, 51.5074, 48.8566, 35.6895],
    'Lon': [-74.0060, -0.1278, 2.3522, 139.6917]
}

df = pd.DataFrame(data)

# Create globe chart
fig = px.scatter_geo(df, lat='Lat', lon='Lon', hover_name='City', projection="natural earth")

# Customize the chart
fig.update_traces(marker=dict(size=10, color='blue', opacity=0.8, symbol='circle'))

# Show the chart
fig.show()