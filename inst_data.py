from yodapy.datasources import OOI
from yodapy.utils.creds import set_credentials_file

#class instData(object):

#    def __init__(self, base_url: str):
#        self.source = 'OOI'

def get_data(username, token, ref_id, t_start, t_end):
    # Default Variables
    data_type = 'json'
    max_samps = 1500
    regions = [x.lower() for x in ["Cabled Array",
                                    "Coastal Endurance",
                                    "Coastal Pioneer",
                                    "Global Argentine Basin",
                                    "Global Irminger Sea",
                                    "Global Southern Ocean",
                                    "Global Station Papa"]]

    # Define the OOI 
    my_data = OOI()
    set_credentials_file(data_source='ooi', username=username, token=token)

    # Send Request
    my_data.search(region=','.join(regions), instrument=ref_id)
    my_data.request_data(begin_date=t_start,
                            end_date=t_end,
                            data_type=data_type,
                            limit=max_samps)

    return my_data.raw()



'''
1) Make an endpoint with this thingy
2) jsonify for return
'''


#https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE04OSBP/LJ01C/06-CTDBPO108/streamed/ctdbp_no_sample?beginDT=&endDT=&limit=1000