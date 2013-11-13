#required imports
import urllib2
import json
import base64
#credentials.py contains the Base64 endocde string
from credentials import development
#from credentials import production
#from credentials import authKey
authKey = base64.b64encode(development)
#authKey = base64.b64encode(production)

#Required URI and request headers
# Un-comment Development or Production
#  Development URL:
url = "https://development.avalara.net/1.0/tax/get"
# Production URL:
#url = "https://avatax.avalara.net/1.0/tax/get"

headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}

#Request body in the form ({"element":"data","element":"data"})
#or use the data.py file which contains a sample json request body
from data import body
data =  (body)

#format data for request
data = json.dumps(data)

#request
request = urllib2.Request(url,data,{'Content-Type': 'application/json'} )
for key,value in headers.items():
    request.add_header(key,value) 

print ""
print "ResultCode:"
print (30 * '-')

#Print results to console
response = urllib2.urlopen(request) 
html = response.read()
print html


