import requests
import pandas as pd
from typing import List, Dict
import numpy as np
import json


def merge_name_rd(row):
    ''' Merges node names and node ref designator '''
    name = row['name'].split('(')[0]
    rd = row['reference_designator'].split('-')[1]
    return f'{name} ({rd})'


def merge_site_name(row):
    ''' Merges site names with ref designator '''
    name = row['name']
    rd = row['reference_designator']
    return f'{name} ({rd})'


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
        url = "{}/nodes.json".format(self.base_url)
        nnames = requests.get(url).json()
        nodes_df = pd.DataFrame.from_records(nnames['nodes'])
        node_names = nodes_df['name']
        node_refIDs = nodes_df['reference_designator']
        nnames = node_names.apply(lambda x: x.split('(')[0])
        return list(np.sort(nodes_df.apply(merge_name_rd, axis=1).unique()))

    def sites(self):
        url = "{}/sites.json".format(self.base_url)
        sites = requests.get(url).json()
        sites_df = pd.DataFrame.from_records(sites)
        return list(np.sort(sites_df.apply(merge_site_name, axis=1).unique()))

    def regions(self):
        url = "{}/regions.json".format(self.base_url)
        regions = requests.get(url).json()
        regions_df = pd.DataFrame.from_records(regions['regions'])
        return list(np.sort(regions_df.apply(merge_site_name, axis=1).unique()))


    def parameter_id(self, param_name: str) -> int:
        """returns the parameter id that matches the provided parameter name.
           -1 is returned if no match is found"""
        url = "{}/parameters.json".format(self.base_url)
        j = requests.get(url).json()
        for r in j['data']:
            if param_name == r['name'] or param_name == r['standard_name'] or param_name == r['display_name']:
                return r['id']
        return -1

    def stream_names(self, parameter_id: int) -> List[str]:
        url = "{}/parameters/view/{}.json".format(self.base_url, parameter_id)
        j = requests.get(url).json()
        names: List[str] = []
        try:
            streams = j['parameter']['streams']
            for s in streams:
                names.append(s['name'])
        except:
            # TODO log or report error?
            pass
        return names

    def reference_designator(self, stream_name: str) -> List[str]:
        url = "{}/streams/view/{}.json".format(self.base_url, stream_name)
        j = requests.get(url).json()
        rds = []
        try:
            designators = j['stream']['data_streams']
            for d in designators:
                rds.append(d['reference_designator'])
        except:
            # TODO log or report error?
            pass
        return rds
