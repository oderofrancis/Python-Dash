import pandas as pd
import dash
# from dash import html
data = pd.read_csv("appstore.csv")

data = (data.assign(review_date=lambda data: pd.to_datetime(data["time"], format="%Y-%m-%d %H:%M:%S")) # Rename and format the review date column
    .sort_values(by="review_date") # Sort by review date
)

external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "App Store Analytics: Understand Your App Reviews!"

app.layout = dash.html.Div(
    children=[
        dash.html.H1(
            children="App Store Analytics",
            className="header-title",
        ),
        dash.html.P(
            children=(
                "Analyze the behavior of app reviews between 2022 and 2023"
            ),
        ),
        dash.dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["review_date"],
                        "y": data["score"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "App Review Scores"},
            },
        ),
        dash.dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["review_date"],
                        "y": data["thumbsUpCount"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Number of Thumbs Up for Reviews"},
            },
        ),
    ],
    className="container",
)

if __name__ == "__main__":
    app.run_server(debug=True)
