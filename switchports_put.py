import json
import requests
import sys
import csv

# Import API key and org ID from login.py
try:
    import login
    (API_KEY, ORG_ID) = (login.api_key, login.org_id)
except ImportError:
    API_KEY = input('Enter your Dashboard API key: ')
    ORG_ID = input('Enter your Organization ID: ')

session = requests.session()
headers = {'X-Cisco-Meraki-API-Key': API_KEY, 'Content-Type': 'application/json'}

# Verify API access is working by pulling the Organization Name, if it fails display error message and exit
try:
    name = json.loads(session.get('https://api.meraki.com/api/v0/organizations/'
                                  + ORG_ID, headers=headers).text)['name']
except:
    sys.exit('Incorrect API key or org ID, as no valid data returned')

# Array of switch serials that will need switchport configurations
switch_serials = ['Q2TP-PQQ2-NLFD', 'Q2DW-WQ9L-M68S', 'Q2DW-LDQP-9HUQ', 'Q2BW-966A-REU2', 'Q2BW-38YF-237D', 'Q2PW-24Z7-ZS6E',
                 'Q2KW-JDTK-AMGG', 'Q2KW-H7KB-GSXX', 'Q2KW-H7QK-AP5D', 'Q2VX-6P9E-Q8YV', 'Q2QW-C6JM-SP77', 'Q2QW-C5UK-A3UE',
                 'Q2QW-CG89-WGEX', 'Q2QW-CFBY-A47Q', 'Q2KW-GU8F-BK3M', 'Q2KW-H8HK-GAJR', 'Q2KW-G6GB-JD2J', 'Q2VX-84JE-9MS3']

csv_columns = ["number", "name", "tags", "enabled", "poeEnabled", "type", "vlan", "voiceVlan", "allowedVlans", "isolationEnabled",
							 "rstpEnabled", "stpGuard", "accessPolicyNumber", "linkNegotiation", "portScheduleId"] 

# Array of switch serials for testing
test_switches = ['Q2MW-244T-ACYT', 'Q2HP-FURK-2ALN']

# Iterate through each switch in the list.
for switch in test_switches:
	csv_file = switch + '.csv'
	# Iterate through each row in the .csv and create a dictionary with the column as the key and the row as the value
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:

			# Create a new list of keys with empty strings in them. This is due to not being able to modify a dictionary 
			# while iterating through it. Then iterate through the list and delete the correpsonding key from the dictionary.
			empty_keys = [k for k,v in row.iteritems() if not v]
			for k in empty_keys:
				del row[k]
			print(row)
			test_request = requests.put('https://api.meraki.com/api/v0/devices/' + switch + '/switchPorts/' + row['number'], headers = headers, data = json.dumps(row)).text
