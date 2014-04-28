#required imports
import sys
import urllib2
import urllib
import json
import base64

## pass credentials to authkey
##('accountNumber:licenseKey') OR
##('userName:password') from Avalara Admin Account

authKey = base64.b64encode('1234567890:A1B2C3D4E5F6G7H8')

##Required URI and request headers
url = "https://development.avalara.net/1.0/tax/cancel"
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}


data = ({
"CompanyCode": 'APITrialCompany',
"DocType" : 'SalesInvoice',
"DocCode" : 'INV001',
"CancelCode" : 'DocVoided',
})

#format data for request
data = json.dumps(data)

#request
request = urllib2.Request(url,data,{'Content-Type': 'application/json'} )
for key,value in headers.items():
   request.add_header(key,value) 
try:
    response = urllib2.urlopen(request)
#Error handling
except urllib2.URLError as e:
    if hasattr(e, 'code'):
        print 'HTTP Error code: ', e.code
        print 'Message: ', e.read()
        sys.exit()
    else: 
        print "Success"
html = response.read()
print html