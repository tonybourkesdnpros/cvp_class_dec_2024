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

config_directory = 'configs'
exists = os.path.exists(config_directory)
if not exists: 
    os.makedirs(config_directory)

current_directory = config_directory+"/"
configlets = client.api.get_configlets(start=0, end=0)

for item in configlets['data']:
    print(f"Writing {item['name']} to a file")
    file_name = item['name']+".txt"
    file = open(current_directory+"/"+file_name, 'w')
    file.write(item['config'])
    file.close()