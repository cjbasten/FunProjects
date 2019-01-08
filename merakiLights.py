import json
import requests
from meraki import meraki


meraki.myorgaccess('3a8cb661bd2076c95db5b093233756610400728e')
org_id = '382029'

url = 'https://api.meraki.com/api/v0/networks/L_637259347272932695/clients/34:7c:25:58:63:a1'
response = requests.get(url)
response.raise_for_status()
