Avatax /Python 2.7 sample requests making use of the Avalara RESTful web service.

What is needed to run these samples is Python 2.7 and an active AvaTax Account. 

If you do not have an AvaTax account you can sign up for a free trial account at: http://developer.avalara.com/api-get-started

For an overview of how AvaTax Calculates tax using our API's visit http://developer.avalara.com/api-docs/designing-your-integration

Samples included are listed below with associated links to documentation:

ValidateRequest.py (http://developer.avalara.com/api-docs/rest/address-validation)

GetTaxRequest.py POST (http://developer.avalara.com/api-docs/rest/tax/post)

CancelTaxRequest.py (http://developer.avalara.com/api-docs/rest/tax/cancel)

Extras:

encode.py is a sample that will convert your account and license key into a base64 string to use as an authKey if desired.

credentials.py  is a safe place to store your account credentials in the form:
development = '110001234:A1B2C3D4E5F6G7'

data.py is a sample GetTaxRequest body that is used by GetTaxRequest.py


For more information on how to calculate tax using AvaTax API as well as some recommended use cases, visit the Avalara Developer's Network at http://developer.avalara.com/api-docs
