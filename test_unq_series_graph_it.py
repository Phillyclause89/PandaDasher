import unittest
from unittest import TestCase
import graph_it
import pandas as pd
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html


class TestUnq_series_graph_it(TestCase):
    def setUp(self) -> None:
        self.valid_ts_df = pd.DataFrame(
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
        self.figure_id = 'test_graph'
        self.series_column = "brand"
        self.y_column = "price"

    def tearDown(self) -> None:
        pass

    def test_unq_series_graph_it(self):
        g_default = graph_it.unq_series_graph_it(
            df=self.valid_ts_df,
            figure_id=self.figure_id,
            series_column=self.series_column,
            y_column=self.y_column,
        )
        base_graph_type = type(dcc.Graph())
        self.assertIsInstance(g_default, base_graph_type)
        self.assertEqual(g_default.id, self.figure_id)
        self.assertEqual(g_default.style, {'height': None, 'width': None})
        app = dash.Dash()
        app.layout = html.Div(children=g_default)
        self.assertIsInstance(app.layout.children, base_graph_type)


if __name__ == "__main__":
    unittest.main()
