import json
import requests
import sys


# Import API key and org ID from login.py
try:
    import login
    (API_KEY, ORG_ID) = (login.api_key, login.org_id)
except ImportError:
    API_KEY = input('Enter your Dashboard API key: ')
    ORG_ID = input('Enter your organization ID: ')

session = requests.session()
headers = {'X-Cisco-Meraki-API-Key': API_KEY, 'Content-Type': 'application/json'}

# Verify API access is working by pulling the Organization Name, if it fails display error message and exit
try:
    name = json.loads(session.get('https://api.meraki.com/api/v0/organizations/'
                                  + ORG_ID, headers=headers).text)['name']
except:
    sys.exit('Incorrect API key or org ID, as no valid data returned')
networks = json.loads(session.get('https://api.meraki.com/api/v0/organizations/'
                                  + ORG_ID + '/networks', headers=headers).text)

# Messing around with comprehensions
NET_ID = [net for network in networks for kv in network.items() for net in kv]

devices = json.loads(session.get('https://api.meraki.com/api/v0/networks/'
                                 + str(NET_ID[1]) + '/devices/', headers=headers).text)

# payload defines up to how many seconds the client could have been associated
payload = {'timespan': 300}

# Could pull inventory of APs and make a list of serials, then iterate through that list in the for loop
ap_one = json.loads(session.get('https://api.meraki.com/api/v0/devices/Q2KD-E8R3-PYQL/clients/',
                                headers=headers, params=payload).text)
ap_two = json.loads(session.get('https://api.meraki.com/api/v0/devices/Q2KD-Z79J-2GM7/clients/',
                                headers=headers, params=payload).text)

roommate_list = ['Corys iPhone', 'Phils iPhone', 'jakes-iPhone', 'Kuhus-iPhone', 'Android']

for i in (ap_one + ap_two):
    if i.get('description') in roommate_list:
        print('Hello, ' + str(i.get('description')))
    else:
        print('Nothing to see here')  # Turn off Philips Hue Bulbs
