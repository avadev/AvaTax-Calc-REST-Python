# Required imports
import sys
import urllib2
import urllib
import json
import base64

# Required Header Parameters
serviceURL = 'https://development.avalara.net'
accountNumber = '1234567890'
licenseKey = 'A1B2C3D4E5F6G7H8'

# Required Request Parameters
data = ({
"CompanyCode": 'APITrialCompany',
"DocType" : 'SalesInvoice',
"DocCode" : 'INV001',
"CancelCode" : 'DocVoided',
})

data = json.dumps(data)

# Build Connector
credentials = accountNumber + ':' + licenseKey
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
resource = '/1.0/tax/cancel'
url = serviceURL + resource 

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
