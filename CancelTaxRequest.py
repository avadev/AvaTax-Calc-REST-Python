#required imports
import sys
import urllib2
import urllib
import json
import base64
#credentials.py contains development = 'account:licensekey'
from credentials import development

# pass credentials to authkey
authKey = base64.b64encode(development)

#Required URI and request headers
url = "https://development.avalara.net/1.0/tax/cancel"
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

#Collect required elements for a CancelTax operation
print (30 * '-')
print "CancelTax Request"
print ""
print (30 * '-')
compccode = raw_input("CompanyCode: ").replace (" ", "+"); 
docttype = raw_input("DocType: ").replace (" ", "+"); 
doccode = raw_input("DocCode: ").replace (" ", "+"); 
cancode = raw_input("CancelCode: ").replace (" ", "+"); 

data = ({
"CompanyCode": compccode,
"DocType" : docttype,
"DocCode" : doccode,
"CancelCode" : cancode,
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