import plotly.express as px
import pandas as pd
import plotly.offline as offline

# Sample data
data = {
    'City': ['Italy', 'Hong Kong', 'Austria', 'Japan', 'France', 'UK', 'Chile', 'United States', 'Hungary', 'Spain', 'Belgium', 'Czech Republic', 'Slovakia', 'Colombia'],
    'Lat': [41.8719, 22.3193, 47.5162, 35.6895, 46.6034, 51.5074, -33.4489, 37.0902, 47.1625, 40.4637, 50.8503, 49.8175, 48.669, 4.711],
    'Lon': [12.5674, 114.1694, 14.5501, 139.6917, 1.8883, -0.1278, -70.6693, -95.7129, 19.5033, -3.7492, 4.4699, 15.472, 19.699, -74.0721]
}
df = pd.DataFrame(data)

# Create globe chart
fig = px.scatter_geo(df, lat='Lat', lon='Lon', hover_name='City', projection="natural earth", title="This is Where I have Traveled")

# Customize the chart
fig.update_traces(marker=dict(size=10, color='purple', opacity=0.8, symbol='circle'))

# Show the chart
fig.show()

offline.plot(fig, filename='plotly_chart.html', auto_open=False)