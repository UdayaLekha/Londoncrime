from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import pandasql as ps


# Load the dataset
df = pd.read_csv('output.csv')
query = ps.sqldf("select borough, major_category, count(major_category) as count_major_crime from df group by borough, major_category")
print(query)
# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=query['borough'].unique(),
                            value='Barnet')

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),
    geo_dropdown,
    dcc.Graph(id='crime-graph')
])


# Set up the callback function
@app.callback(
    Output(component_id='crime-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_crime = query[query['borough'] == selected_geography]
    line_fig = px.bar(filtered_crime,
                       x='major_category', y='count_major_crime',
                       color='major_category',
                       title=f'Major crimes in {selected_geography}')
    return line_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)