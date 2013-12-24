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

#Collect address from User input - replace white space with '+'
print ""
print "Enter Address to be Validated"
print (30 * '-')
l1 = raw_input("Line1: ").replace (" ", "+"); 
l2 = raw_input("Line2: ").replace (" ", "+"); 
l3 = raw_input("Line3: ").replace (" ", "+"); 
c = raw_input("City: ").replace (" ", "+"); 
r = raw_input("Region: ").replace (" ", "+"); 
z = raw_input("PostalCode: ").replace (" ", "+"); 
cnt = raw_input("CountryCode: ").replace (" ", "+"); 

#show address entered
print ""
print "Address Entered: "
print l1, l2, l3, c, r, z, cnt;

#construct URL from data collected above
url = ('https://development.avalara.net/1.0/address/validate?Line1='+l1+'&Line2='+l2+'&Line3='+l3+'&City='+c+'&Region='+r+'&PostalCode='+z+'&Country='+cnt)

#request
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
request = urllib2.Request(url)
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
