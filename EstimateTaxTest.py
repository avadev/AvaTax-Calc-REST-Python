# Required Imports
import sys
import urllib2
import urllib
import json
import base64
from credentials import serviceURL, accountNumber, licenseKey

# Required Request Parameters
latitude = '47.627935'
longitude = '-122.51702'
request = 'saleamount='
saleAmount = '10.00'

# Build Connector
credentials = accountNumber + ':' + licenseKey
coordinates = latitude + ',' + longitude
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
resource = '/1.0/tax/'
url = serviceURL + resource + coordinates + '/get?' + request + saleAmount

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
