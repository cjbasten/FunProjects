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
try:
    name = json.loads(session.get('https://api.meraki.com/api/v0/organizations/' + ORG_ID, headers=headers).text)['name']
except:
    sys.exit('Incorrect API key or org ID, as no valid data returned')
networks = json.loads(session.get('https://api.meraki.com/api/v0/organizations/' + ORG_ID + '/networks', headers=headers).text)
NET_ID = [v for network in networks for k, v in network.items()]
inventory = json.loads(session.get('https://api.meraki.com/api/v0/organizations/' + ORG_ID + '/inventory', headers=headers).text)
appliances = [device for device in inventory if device['model'][:2] in ('MX', 'Z1', 'Z3', 'vM') and device['networkId'] is not None]
devices = [device for device in inventory if device not in appliances and device['networkId'] is not None]
payload = {'timespan':50}
clients = json.loads(session.get('https://api.meraki.com/api/v0/devices/Q2KD-E8R3-PYQL/clients/', headers=headers, params=payload).text)

print(devices)
print(NET_ID)
print(clients)