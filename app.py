

if __name__ == '__main__':
    import dash
    import pandas as pd
    import datetime as dt
    import dash_html_components as html
    from dash.dependencies import Input, Output
    from dash.exceptions import PreventUpdate
    from graph_it import unq_series_graph_it

    """DATA_FRAME:
        Test DF hopefully you can replace it with your own df 
        and the series_graph_it(...) func will work 
        on the use case you described.

    """
    DATA_FRAME = pd.DataFrame(
        {
            'date': [
                dt.datetime.strptime(
                    date,
                    "%m/%d/%Y"
                ).date() for date in [
                    "10/24/2019", "10/24/2019", "10/25/2019", "10/25/2019",
                    "10/26/2019", "10/26/2019", "10/27/2019", "10/27/2019",
                ]
            ],
            'name': ["a", "b", "a", "b", "a", "b", "a", "b"],
            'brand': ["a", "b", "a", "b", "a", "b", "a", "b"],
            'retailer': ["ra", "ra", "ra", "ra", "ra", "ra", "ra", "ra"],
            'price': [8.99, 6.99, 8.59, 6.50, 9.50, 2.30, 9.50, 0.5],
            'stars': [4.5, 4.3, 4.4, 4.0, 4.9, 2.2, 4.8, 1.8],
            'category': ["ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca"],
            'highlights': ["_", "_", "_", "_", "_", "_", "_", "_"]
        }
    ).set_index('date')
    """Dash Layout Source:
        <a href="https://dash.plot.ly/getting-started">Basic Dash App</a>
    """
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', ]
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets, )
    # >>> Example call of series_graph_it(...) func
    app.layout = html.Div(
        # ...
        children=[
            html.H1(children='Dashboard Title'),
            html.Div(children="Dashboard description text."),
            # ...
            html.Div(
                id="graph-div",
                # ...
                children=unq_series_graph_it(
                    df=DATA_FRAME,
                    figure_id='my-graph',
                    series_column="brand",
                    y_column="price"
                )
            ),
        ],
    )


    # Easter Egg callback
    @app.callback(
        Output(component_id='graph-div', component_property='children'),
        [Input(component_id='graph-div', component_property='n_clicks')]
    )
    def refresh(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
        else:
            return unq_series_graph_it(
                df=DATA_FRAME,
                figure_id='my-graph',
                series_column="brand",
                y_column="price"
            )


    app.run_server(debug=True)