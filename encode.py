import base64
#assumes that account:license key or username:password are identified as 
# key "development" in credentials.py
from credentials import development
authKey = base64.b64encode(development)
print  "The following key can be used in place of the var authKey where ever it appears in this sample code set"
print (30 * '-')
print authKey

