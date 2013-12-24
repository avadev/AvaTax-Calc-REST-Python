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
url = "https://development.avalara.net/1.0/tax/get"
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

#Request body in the form ({"element":"data","element":"data"}) - OR
#import json sample from data.py
from data import body
data =  data =  ({
    "DocDate": "2013-12-23",
    "CompanyCode": "",
    "CustomerCode": "AvaTax",
    "DocCode": "220131223-3",
    "DocType": "SalesOrder",
    "Commit": "false",
    "Addresses": 
    [
    {
        "AddressCode": "1",
        "Line1": "435 Ericksen Avenue Northeast",
        "Line2": "#250",
        "City": "Bainbridge Island",
        "Region": "AK",
        "PostalCode": "98110",
        "Country": "US",
    },
    {                
        "AddressCode": "2",
        "Line1": "100 Ravine lane",
        "Line2": "#220",
        "City": "Bainbridge Island",
        "Region": "AK",
        "PostalCode": "98110",
        "Country": "US",
        }
    ],
    "Lines": 
    [
    {
        "LineNo": "1",
        "DestinationCode": "2",
        "OriginCode": "1",
        "ItemCode": "AvaDocs",
        "Description": "Box of Avalara Documentation",
        "Qty": "1",
        "Amount": "100",
    },
    ],
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
