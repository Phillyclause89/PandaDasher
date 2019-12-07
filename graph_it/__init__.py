# noinspection SpellCheckingInspection
"""graph_it:
Functions that return dash_core_components.Graph

TODO:
    * @Noarfang:
        * Replace your DF with my test df and let me know if it works.
    * @Me:
        * Finish docstrings
        * Make dope lib of other plot functions
LICENSES:
    * dash:
        The MIT License (MIT)

        Copyright (c) 2019 Plotly, Inc

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in
        all copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
        THE SOFTWARE.
    * pandas:
        BSD 3-Clause License

        Copyright (c) 2008-2012, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
        All rights reserved.

        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:

        * Redistributions of source code must retain the above copyright notice, this
          list of conditions and the following disclaimer.

        * Redistributions in binary form must reproduce the above copyright notice,
          this list of conditions and the following disclaimer in the documentation
          and/or other materials provided with the distribution.

        * Neither the name of the copyright holder nor the names of its
          contributors may be used to endorse or promote products derived from
          this software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
        AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
        IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
        FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
        DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
        SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
        CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
        OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
        OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

DOCS:
    https://htmlpreview.github.io/?https://github.com/Phillyclause89/PandaDasher/blob/master/html/graph_it.html

"""

import random

import dash
import dash_core_components as dcc


def unq_series_graph_it(df, figure_id, series_column, y_column, height=None, width=None):
    # noinspection SpellCheckingInspection
    """unq_series_graph_it(df, figure_id, series_column, y_column, height=None, width=None):

        Function for returning a multi series <dash_core_components.Graph object>
        from a df with the series values in the same column.

        Examples:

            Example dashboard using graph_it.unq_series_graph_it(): https://graph-it-demo-app.herokuapp.com/

            >>> import dash
            >>> import pandas as pd
            >>> import datetime as dt
            >>> import dash_html_components as html
            >>> from dash.dependencies import Input, Output
            >>> from dash.exceptions import PreventUpdate
            >>> from graph_it import unq_series_graph_it
            >>> from flask import Flask
            >>>
            >>> # noinspection PyUnresolvedReferences
            ... DATA_FRAME = pd.DataFrame(
            ...     {
            ...         'date': [
            ...             dt.datetime.strptime(
            ...                 date,
            ...                 "%m/%d/%Y"
            ...             ).date() for date in [
            ...                 "10/24/2019", "10/24/2019", "10/25/2019", "10/25/2019",
            ...                 "10/26/2019", "10/26/2019", "10/27/2019", "10/27/2019",
            ...             ]
            ...         ],
            ...         'name': ["a", "b", "a", "b", "a", "b", "a", "b"],
            ...         'brand': ["a", "b", "a", "b", "a", "b", "a", "b"],
            ...         'retailer': ["ra", "ra", "ra", "ra", "ra", "ra", "ra", "ra"],
            ...         'price': [8.99, 6.99, 8.59, 6.50, 9.50, 2.30, 9.50, 0.5],
            ...         'stars': [4.5, 4.3, 4.4, 4.0, 4.9, 2.2, 4.8, 1.8],
            ...         'category': ["ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca"],
            ...         'highlights': ["_", "_", "_", "_", "_", "_", "_", "_"]
            ...     }
            ... ).set_index('date')
            >>> server = Flask(__name__)
            >>> external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', ]
            >>> app = dash.Dash(name=__name__, server=server,
            ...                 external_stylesheets=external_stylesheets, )
            ...
            >>> # >>> Example call of series_graph_it(...) func
            >>> # noinspection PyUnresolvedReferences
            ... app.layout = html.Div(
            ...     # ...
            ...     children=[
            ...         html.H1(children='Dashboard Title'),
            ...         html.Div(children="Dashboard description text."),
            ...         # ...
            ...         html.Div(
            ...             id="graph-div",
            ...             # ...
            ...             children=unq_series_graph_it(
            ...                 df=DATA_FRAME,
            ...                 figure_id='my-graph',
            ...                 series_column="brand",
            ...                 y_column="price"
            ...             )
            ...         ),
            ...     ],
            ... )
            >>>
            >>>
            >>> # Easter Egg callback
            >>> @app.callback(
            ...     Output(component_id='graph-div', component_property='children'),
            ...     [Input(component_id='graph-div', component_property='n_clicks')])
            ... def refresh(n_clicks):
            ...     # noinspection PyUnresolvedReferences
            ... if n_clicks is None:
            ...         raise PreventUpdate
            ...     else:
            ...         return unq_series_graph_it(
            ...             df=DATA_FRAME,
            ...             figure_id='my-graph',
            ...             series_column="brand",
            ...             y_column="price"
            ...         )
            >>>
            >>>
            >>> if __name__ == '__main__':
            ...     app.run_server(debug=False)
            ...







        Args:
            df: (pandas.DataFrame) REQUIRED:
            figure_id: (str) REQUIRED:
            series_column: (str) REQUIRED:
            y_column: (str) REQUIRED:
            height: (int) Optional:
            width: (int) Optional:

        Returns:
            (dash_core_components.Graph)

        """
    unq = df[series_column].unique()
    x_df_l = [df[df[series_column] == x] for x in unq]
    data_l = []
    for i, d in enumerate(x_df_l):
        data_l.append(
            dict(
                x=d[y_column].keys(),
                y=d[y_column].values,
                name=f'{unq[i]} {y_column}',
                marker=dict(
                    color=f'rgb('
                    f'{random.randint(0, 255)}, '
                    f'{random.randint(0, 255)}, '
                    f'{random.randint(0, 255)})',
                ),
            )
        )
    # noinspection PyPep8
    return dcc.Graph(
        figure=dict(
            data=data_l,
            layout=dict(
                title=f'{unq} {y_column} over time',
                margin=dict(l=40, r=0, t=40, b=30)
            )
        ),
        style={
            'height': height,
            'width': width
        },
        id=figure_id
    )
