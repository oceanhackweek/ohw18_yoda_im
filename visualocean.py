import requests
import pandas as pd
import numpy as np


def merge_name_rd(row):
    ''' Merges node names and node ref designator '''
    name = row['name'].split('(')[0]
    rd = row['reference_designator'].split('-')[1]
    return f'{name} ({rd})'

def merge_site_name(row):
    ''' Merges site names with ref designator '''
    name = row['name']
    rd   = row['reference_designator']
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
        url = "{}/nodes.json".format(self.base_url)
        nnames = requests.get(url).json()
        nodes_df    = pd.DataFrame.from_records(nnames['nodes'])
        node_names  = nodes_df['name']
        node_refIDs = nodes_df['reference_designator']
        nnames = node_names.apply(lambda x: x.split('(')[0])
        return list(np.sort(nodes_df.apply(merge_name_rd, axis=1).unique()))

    def sites(self):
        url = "{}/sites.json".format(self.base_url)
        sites = requests.get(url).json()
        sites_df = pd.DataFrame.from_records(sites)
        return list(np.sort(sites_df.apply(merge_site_name, axis=1).unique()))



