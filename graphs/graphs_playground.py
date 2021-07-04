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


nests19 = [34,155,180,41,0,0]
nests20 = [14,144,170,10,0,0]
month = ["oct","Nov","Dec","Jan","Feb","Mar"]

fig = go.Figure(data=[
    go.Scatter(
        name="Nests 19",
        x=month,
        y=nests19
    ),
    go.Scatter(
        name="Nests 20",
        x=month,
        y=nests20
    )
])

fig.update_layout(
    title="Overall Stats",
    xaxis_title="Statistic",
    yaxis_title="Number Recorded"
)
fig.add_layout_image(
dict(
    source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
    xref="paper", yref="paper",
    x=1, y=1.05,
    sizex=0.2, sizey=0.2,
    xanchor="right", yanchor="bottom"
)
)

fig.write_html("nest_demo.html")
