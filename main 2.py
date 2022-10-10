from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import pandasql as ps

# Load the dataset
df = pd.read_csv('output2.csv')
query = ps.sqldf(
    "select perc_change, no_crimes_2016, count(no_crimes_2016) as count_no_crimes_2016 from df group by perc_change, no_crimes_2016")
print(query)
# Create the Dash app
app = Dash()

# Set up the app layout
geo_dropdown = dcc.Dropdown(options=query['perc_change'].unique(),
                            value='Brent')

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),
    geo_dropdown,
    dcc.Graph(id='crime-graph 2')
])


# Set up the callback function
@app.callback(
    Output(component_id='crime-graph 2', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    df.loc[df['no_crimes_2016'] > 2.e6, 'borough'] = 'Other boroughs'
    fig = px.pie(df, values='no_crimes_2016', names='borough', title='Percentage change in no_crimes_2016')
    fig.show()
    return fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)

