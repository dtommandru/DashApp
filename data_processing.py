import base64
import datetime
import io

import pandas as pd

import dash_html_components as html
import dash_table_experiments as dt



class DataProcessing:
    """docstring forDataProcessing."""
    def __init__(self, contents, filename, date):
        self.contents = contents
        self.filename = filename
        self.date = date

    def parse_contents(self,contents, filename, date):
        self.contents = contents
        self.filename = filename
        self.date = date
        print("hello")
        content_type, content_string = self.contents.split(',')

        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in self.filename:
            # Assume that the user uploaded a CSV file
                self.df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in self.filename:
            # Assume that the user uploaded an excel file
                self.df = pd.read_excel(io.BytesIO(decoded))
        except Exception as e:
            print(e)
            return html.Div([
                'There was an error processing this file.'
            ])

        return html.Div([
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(self.date)),

            # Use the DataTable prototype component:
            # github.com/plotly/dash-table-experiments
            dt.DataTable(rows=self.df.head(20).to_dict('records')),

            html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
            html.Div('Raw Content'),
            html.Pre(self.contents[0:200] + '...', style={
                'whiteSpace': 'pre-wrap',
                'wordBreak': 'break-all'
            })
        ])
    def eda(self):
        pass
