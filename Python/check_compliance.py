from cvprac.cvp_client import CvpClient
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = '192.168.0.5'
cvp_user = 'arista'
cvp_pass = 'arista4851'

client = CvpClient()

client.connect([cvp1], cvp_user, cvp_pass)

inventory = client.api.get_inventory()

for item in inventory:
    if item['complianceIndication'] == 'WARNING':
        print(f"{item['hostname']} is not in compliance")