# Required imports
import sys
import urllib2
import urllib
import json
import base64

# Required Parameters
hostName = 'https://development.avalara.net'
resource = '/1.0/tax/'
method = 'cancel'

# Required Credentials
accountNumber = '1234567890'
licenseKey = 'A1B2C3D4E5F6G7H8''
credentials = accountNumber + ':' + licenseKey

# Required Data Elements
data = ({
"CompanyCode": 'timzoffice',
"DocType" : 'SalesInvoice',
"DocCode" : '100000',
"CancelCode" : 'DocVoided',
})

# Format data for request
data = json.dumps(data)

# Build Connector
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

# Build URI
url = hostName + resource + method  

# Submit Request
cancelTaxRequest = urllib2.Request(url, data, {'Content-Type': 'application/json'})
for key, value in headers.items():
   cancelTaxRequest.add_header(key, value) 
try:
    response = urllib2.urlopen(cancelTaxRequest)

# Error handling
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
