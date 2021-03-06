# required imports
import sys
import urllib2
import urllib
import json
import base64
from credentials import serviceURL, accountNumber, licenseKey

# Required Request Parameters
Line1 = '118 N Clark St'
Line2 = 'Suite 100'
Line3 = 'ATTN Accounts Payable'
City = 'Chicago'
Region = 'IL'
PostalCode = '60602'
Country = 'US'

# Construct Address String
line1 = Line1.replace (" ", "+"); 
line2 = Line2.replace (" ", "+"); 
line3 = Line3.replace (" ", "+"); 
city = City.replace (" ", "+"); 
region = Region.replace (" ", "+"); 
postalCode = PostalCode.replace (" ", "+"); 
country = Country.replace (" ", "+"); 
setAddress = ('?&Line1=' + line1 + '&Line2=' + line2 + '&Line3=' + line3 
              + '&City=' + city + '&Region=' + region + '&PostalCode=' + postalCode 
              + '&Country=' + country)

# Build Connector
credentials = accountNumber + ':' + licenseKey
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
resource = '/1.0/address/validate'
url = serviceURL + resource 

# Submit Request
validateAddressRequest = urllib2.Request(url + setAddress)
for key, value in headers.items():
   validateAddressRequest.add_header(key, value) 
try:
    response = urllib2.urlopen(validateAddressRequest)

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