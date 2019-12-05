import unittest
from unittest import TestCase
import graph_it
import pandas as pd
import datetime as dt
import dash
import dash_core_components as dcc
import dash_html_components as html


class TestUnq_series_graph_it(TestCase):
    def test_unq_series_graph_it(self):
        data_frame = pd.DataFrame(
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
        g = graph_it.unq_series_graph_it(
            df=data_frame,
            figure_id='my-graph',
            series_column="brand",
            y_column="price"
        )
        base_graph_type = type(dcc.Graph())
        self.assertIsInstance(g, base_graph_type)
        self.assertEqual(g.id, 'my-graph')
        app = dash.Dash()
        app.layout = html.Div(children=g)
        self.assertIsInstance(app.layout.children, base_graph_type)
        print("\n", type(app.layout.children))

        # self.assertEqual()


if __name__ == "__main__":
    unittest.main()
