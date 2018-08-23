import requests
import pandas as pd


def merge_name_rd(row):
    ''' Merges node names and node ref designator '''
    name = row['name'].split('(')[0]
    rd = row['reference_designator'].split('-')[1]
  
    return f'{name} ({rd})'

class VisualOcean(object):

    def __init__(self, base_url):
        self.base_url = base_url

    def products(self):
        url = "{}/parameters.json".format(self.base_url)
        json = requests.get(url).json()
        df = pd.DataFrame.from_records(json['data'])
        science_df = df[df.data_product_type == 'Science Data']
        all_params = list(science_df['display_name'].dropna().values) + list(
            science_df['name'].dropna().values) + list(science_df['standard_name'].dropna().values)
        return sorted(list(set(all_params)))

    def instruments(self):
        url = "{}/instruments.json".format(self.base_url)
        params = requests.get(url).json()
        df = pd.DataFrame.from_records(params['data'])
        return sorted(list(set(df['name'].dropna().values)))

    def nodes(self):
        nodes    = requests.get('/'.join([base_url, 'nodes.json'])).json()
        nodes_df = pd.DataFrame.from_records(nodes['nodes'])
        unique_nodes = sorted(list(set(nodes_df['name'].dropna().values)))

