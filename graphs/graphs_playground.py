import plotly.graph_objects as go
#go and get graph objects from plotly and call it "go"

years = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
perth_population = [1.67, 1.83, 1.97, 2.02, 2.04, 2.14, 2.20, 2.28, 2.385, 2.47]
brisbane_population = [1.98, 2.10, 2.24, 2.27, 2.3, 2.38, 2.42, 2.48, 2.56, 2.62]
adelaide_population = [1.198, 1.251, 1.29, 1.3, 1.316, 1.34, 1.36, 1.38, 1.408, 1.429]

fig = go.Figure(data=[
    go.Bar(
        name="Perth",
        x=years,
        y=perth_population
    ),
    go.Bar(
        name="Brisbane",
        x=years,
        y=perth_population
    )
])

fig.write_html("bargraph.html")