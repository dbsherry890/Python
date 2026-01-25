import dash
from dash import html
import dash_mantine_components as dmc
from dash import html, Input, Output, State

app = dash.Dash(__name__)

app.layout = dmc.MantineProvider(
    children=dmc.Container(
        size="sm",
        children=[
            dmc.Title("Dash Mantine Example", order=2),
            dmc.Space(h=20),

            dmc.TextInput(
                id="input-text",
                label="Enter some text",
                placeholder="Type something...",
            ),
            dmc.Space(h=10),

            dmc.Button("Submit", id="submit-button", color="indigo"),
            dmc.Space(h=20),

            dmc.Text(id="output-text", size="lg")
        ]
    )
)


@app.callback(
    Output("output-text", "children"),
    Input("submit-button", "n_clicks"),
    State("input-text", "value"),
    prevent_initial_call=True,
)
def update_text(n_clicks, value):
    return f"You entered: {value}" if value else "No input provided."


if __name__ == "__main__":
    app.run(debug=True)
