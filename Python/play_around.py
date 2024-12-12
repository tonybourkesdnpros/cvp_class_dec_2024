from cvprac.cvp_client import CvpClient
import requests
import os

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = '192.168.0.5'
cvp_user = 'arista'
cvp_pass = 'arista4851'

client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pass)

device = client.api.get_device_by_name('leaf4.atd.lab')
mac = device['systemMacAddress']
configlets = client.api.get_configlets_by_device_id(mac)

for item in configlets:
    print(item['name'])