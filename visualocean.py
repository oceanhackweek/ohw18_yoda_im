import requests
import pandas as pd
from typing import List


class VisualOcean(object):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def products(self) -> List[str]:
        url = "{}/parameters.json".format(self.base_url)
        json = requests.get(url).json()
        df = pd.DataFrame.from_records(json['data'])
        science_df = df[df.data_product_type == 'Science Data']
        all_params = list(science_df['display_name'].dropna().values) + list(
            science_df['name'].dropna().values) + list(science_df['standard_name'].dropna().values)
        return sorted(list(set(all_params)))

    def instruments(self) -> List[str]:
        url = "{}/instruments.json".format(self.base_url)
        params = requests.get(url).json()
        df = pd.DataFrame.from_records(params['data'])
        return sorted(list(set(df['name'].dropna().values)))

    def nodes(self) -> List[str]:
        nodes    = requests.get('/'.join([base_url, 'nodes.json'])).json()
        nodes_df = pd.DataFrame.from_records(nodes['nodes'])
        unique_nodes = sorted(list(set(nodes_df['name'].dropna().values)))

