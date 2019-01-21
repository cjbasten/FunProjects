import json
import requests
import sys


# Import API key and org ID from login.py
try:
    import login
    (API_KEY, ORG_ID, HUE_USER, HUE_IP) = (login.api_key, login.org_id, login.hue_user, login.hue_ip)
    HUE_URL = 'http://'+HUE_IP+'/api/'+HUE_USER+'/'
except ImportError:
    API_KEY = input('Enter your Dashboard API key: ')
    ORG_ID = input('Enter your Organization ID: ')
    HUE_USER = input('Enter your Philips Hue Username')
    HUE_IP = input('Enter your Philips Hue IP')
    HUE_URL = 'http://' + HUE_IP + '/api/' + HUE_USER + '/'

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
payload = {'timespan': 120}

# Could pull inventory of APs and make a list of serials, then iterate through that list in the for loop
ap_one = json.loads(session.get('https://api.meraki.com/api/v0/devices/Q2KD-E8R3-PYQL/clients/',
                                headers=headers, params=payload).text)
ap_two = json.loads(session.get('https://api.meraki.com/api/v0/devices/Q2KD-Z79J-2GM7/clients/',
                                headers=headers, params=payload).text)

roommate_list = ['Corys iPhone', 'Phils iPhone', 'jakes-iPhone', 'Kuhus-iPhone', 'Android']
client_list = [client.get('description') for client in (ap_one + ap_two)]

# philips_hue = json.loads(session.get('http://' + HUE_IP + '/api/' + HUE_USER + '/lights').text)
# print(philips_hue)

number_of_lights = 20
blacklist_lights = set([2, 3, 4, 5])
light_list = set(range(1, number_of_lights))
# print(light_list - blacklist_lights)
# Turn off lights if roommates list does not intersect with client list

#get groups from hue
groups = session.get(HUE_URL + 'groups').json()
print(groups.items())
for k, v in groups.items():
    for j, h in v.items():
        if j == 'name' or 'lights':
            print(k)
            print(h)

'''
{'phils room' -> {id: 1, lights: [2,3,4,5]}},
{'corys room' -> {id: 7, lights: [18.19]}}

if groups.get(phils room) != None

'''

if len(set(client_list).intersection(set(roommate_list))) == 0:
    print("ain't nothing in this list, yo")
    for i in range(light_list - blacklist_lights):
        turn_off_light = session.put(HUE_URL + 'lights/' + str(i) + '/state',
                                     json={"on": False})
else:
    if len(set(client_list).intersection(set(roommate_list))) == 1:
        for i in range(20):
            turn_on_light = session.put(HUE_URL + 'lights/' + str(i) + '/state',
                                        json={"on": True})

# TO DO
# Integrate with OAuth to allow for polling lights outside of network
# Deploy to Phil's web server
# Phil asked for his lights to be blacklisted
