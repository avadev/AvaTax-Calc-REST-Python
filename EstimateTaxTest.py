# Required Imports
import sys
import urllib2
import urllib
import json
import base64

# Required Parameters
hostName = 'https://development.avalara.net'
resource = '/1.0/tax/'
method = '/get?'

# Required Credentials
accountNumber = '1234567890'
licenseKey = 'A1B2C3D4E5F6G7H8''
credentials = accountNumber + ':' + licenseKey

# Address Coordinates
latitude = '47.627935'
longitude = '-122.51702'
coordinates = latitude + ',' + longitude

# Request Parameters
request = 'saleamount='
saleAmount = '10.00'

# Build Connector
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

# Build URI
url = hostName + resource + coordinates + method + request + saleAmount

# Submit Request
estimateRequest = urllib2.Request(url)
for key, value in headers.items():
   estimateRequest.add_header(key, value) 
try:
    response = urllib2.urlopen(estimateRequest)

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
print 'Complete URI Passed:  ' + url
