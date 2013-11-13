#required imports
import urllib2
import json
import base64
#get account:licensekey or username:password combination from credentials.py
#choose development or produciton
from credentials import development

#from credentials import authKey
authKey = base64.b64encode(development)
print authKey
#Required URI and request headers
url = "https://development.avalara.net/1.0/tax/cancel"
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

#Request body in the form ({"element":"data","element":"data"})
#Collect address from User input - replace white space with '+'
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

#Print results to console
response = urllib2.urlopen(request) 
html = response.read()
print html


