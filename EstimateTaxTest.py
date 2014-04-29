# Required Imports
import sys
import urllib2
import urllib
import json
import base64

# Required Parameters
url = 'https://development.avalara.net/1.0/tax/'
accountNumber = '1234567890'
licenseKey = 'A1B2C3D4E5F6G7H8''
latitude = '47.627935'
longitude = '-122.51702'
saleAmount = '10.00'

# Build Connector
credentials = accountNumber + ':' + licenseKey
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

# Build Data String
coordinates = latitude + ',' + longitude
collection = coordinates + '/' + 'get?saleamount=' + saleAmount

# Submit Request
request = urllib2.Request(url + collection)
for key, value in headers.items():
   request.add_header(key, value) 
try:
    response = urllib2.urlopen(request)

# Results and Error Handling
except urllib2.URLError as e:
    if hasattr(e, 'code'):
        print 'HTTP Error code: ', e.code
        print 'Message: ', e.read()
        sys.exit()
    else: 
        print "Success"
html = response.read()
print html