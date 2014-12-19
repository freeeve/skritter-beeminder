from base64 import b64encode
import json
import urllib
import urllib2
from datetime import date,timedelta

url = 'https://www.skritter.com/api/v0/oauth2/token'
OAUTH_CLIENT_NAME = os.environ['SKRITTER_API_USER'] # have to create a separate account (APICLIENT coupon code)
OAUTH_CLIENT_SECRET = os.environ['SKRITTER_API_SECRET'] # get from client page

USER_NAME = os.environ['SKRITTER_USER']     # whose account you want access to
USER_PASSWORD = os.environ['SKRITTER_PASS']       # get from user input, don't store it

params = {
	'grant_type':  'password',
	'client_id':   OAUTH_CLIENT_NAME,
	'username':    USER_NAME,
	'password':    USER_PASSWORD,
	}
credentials = "%s:%s" % (OAUTH_CLIENT_NAME, OAUTH_CLIENT_SECRET)
credentials = b64encode(credentials)
credentials = "basic %s" % credentials

data = urllib.urlencode(params)
request = urllib2.Request(url, data)

# urllib2 apparently prepends HTTP_, your mileage may vary
request.add_header('AUTHORIZATION', credentials)

response = urllib2.urlopen(request)
packet = json.loads(response.read())
token = packet.get('access_token')
params = {
	'start':(date.today() - timedelta(hours=24)).isoformat(),
	'lang':'ja',
	'bearer_token':token
}
data = urllib.urlencode(params)
req2 = urllib2.Request("https://www.skritter.com/api/v0/progstats?%s" % (data))
resp = urllib2.urlopen(req2)
buf = resp.read()
packet = json.loads(buf)
studied = packet['ProgressStats'][0]['timeStudied']['day']

print(int(studied//60))
params = {
	'minutesStudied':int(studied//60)
}
data = urllib.urlencode(params)
req3 = urllib2.Request("https://zapier.com/hooks/catch/ozx9ov/", data)
resp = urllib2.urlopen(req3)
