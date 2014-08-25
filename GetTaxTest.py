# Required Imports
import sys
import urllib2
import urllib
import json
import base64
from credentials import serviceURL, accountNumber, licenseKey

# Required Request Parameters
data = ({                
"CustomerCode": "ABC4335",
"DocDate": "2014-01-01",
"CompanyCode": "APITrialCompany",
"Client": "AvaTaxSample",
"DocCode": "INV001",
"DetailLevel": "Tax",
"Commit": "false",
"DocType": "SalesInvoice",
# Situational Request Document Parameters
# "CustomerUsageType": "G",
# "ExemptionNo": "12345",
# "Discount": "50",
# "TaxOverride": {
#    "TaxOverrideType": "TaxDate",
#    "Reason": "Adjustment for return",
#    "TaxDate": "2013-07-01",
#    "TaxAmount": "0",
#   },

# Optional Request Parameters
"PurchaseOrderNo": "PO123456",
"ReferenceCode": "ref123456",
"PosLaneCode": "09",
"CurrencyCode": "USD",
"Addresses": [
{
    "AddressCode": "01",
    "Line1": "45 Fremont Street",
    "City": "San Francisco",
    "Region": "CA"    },


{
    "AddressCode": "02",
    "Line1": "118 N Clark St",
    "Line2": "Suite 100",
    "Line3": "ATTN Accounts Payable",
    "City": "Chicago",
    "Region": "IL",
    "Country": "US",
    "PostalCode": "60602"    },


{
    "AddressCode": "03",
    "Latitude": "47.627935",
    "Longitude": "-122.51702"    }


],
"Lines": [
{
    "LineNo": "01",
    "ItemCode": "N543",
    "Qty": "1",
    "Amount": "10",
    "OriginCode": "01",
    "DestinationCode": "02",
    "Description": "Red Size 7 Widget",
    "TaxCode": "NT",
# Situational Request Parameters
#    "CustomerUsageType": "L",
#    "Discounted": "true",
#    "TaxIncluded": "true",
#    "TaxOverride":
#    {
#        "TaxOverrideType": "TaxDate",
#        "Reason": "Adjustment for return",
#        "TaxDate": "2013-07-01",
#        "TaxAmount": "0"        },
    "Ref1": "ref123",
    "Ref2": "ref456"    },
{
    "LineNo": "02",
    "ItemCode": "T345",
    "Qty": "3",
    "Amount": "150",
    "OriginCode": "01",
    "DestinationCode": "03",
    "Description": " Size 10 Green Running Shoe",
    "TaxCode": "PC030147"    },
{
    "LineNo": "02-FR",
    "ItemCode": "FREIGHT",
    "Qty": "1",
    "Amount": "15",
    "OriginCode": "01",
    "DestinationCode": "03",
    "Description": "Shipping Charge",
    "TaxCode": "FR"    },
    ],
})

# Format data 
data = json.dumps(data)

# Build Connector
credentials = accountNumber + ':' + licenseKey
authKey = base64.b64encode(credentials)
headers = {"Content-Type":"application/json", "Authorization":"Basic " + authKey}
resource = '/1.0/tax/get'
url = serviceURL + resource 

# Submit Request
getTaxRequest = urllib2.Request(url, data, {'Content-Type': 'application/json'})
for key, value in headers.items():
   getTaxRequest.add_header(key, value) 
try:
    response = urllib2.urlopen(getTaxRequest)

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
