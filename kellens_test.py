from yodapy.datasources import OOI
from yodapy.utils.creds import set_credentials_file


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
    
    print(' ')

    # Define the OOI 
    my_data = OOI()
    print('Setting credentials...', end='')
    set_credentials_file(data_source='ooi', username=username, token=token)
    print(' Done!')

    # Send Request
    print('Searching for instrument...', end='')
    my_data.search(region=','.join(regions), instrument=ref_id)
    print(' Done!')

    print('Sending request...', end='')
    my_data.request_data(begin_date=t_start,
                               end_date=t_end,
                               data_type=data_type,
                               limit=max_samps)
    print(' Done!')

    return my_data.raw()


#def main():
print('hello')
username = 'OOIAPI-D8S960UXPK4K03'
token = 'IXL48EQ2XY'
refID = 'CE04OSBP-LJ01C-06-CTDBPO108'
data = get_data(username,token,refID,'2017-08-22T00:00:00.000Z','2017-08-23T04:00:00.000Z')
data


'''
1) Make an endpoint with this thingy
2) jsonify for return
'''


#https://ooinet.oceanobservatories.org/api/m2m/12576/sensor/inv/CE04OSBP/LJ01C/06-CTDBPO108/streamed/ctdbp_no_sample?beginDT=&endDT=&limit=1000