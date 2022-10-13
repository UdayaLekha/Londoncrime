import pandas as pd
import plotly.express as px
import pandasql as ps

df = pd.read_csv('output3.csv')
query = ps.sqldf(
    "select perc_change, no_crimes_2016, count(no_crimes_2016) as count_no_crimes_2016 from df group by perc_change, no_crimes_2016")
print(query)
fig = px.line(df, x='no_crimes_2011', y='perc_change', color='borough', markers=True)
fig.show()


