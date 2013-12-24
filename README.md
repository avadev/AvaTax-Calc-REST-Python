Avatax /Python 2.7 sample requests making use of the Avalara RESTful web service.

What is needed to run these samples is Python 2.7 and an active AvaTax Account. 

If you do not have an AvaTax account you can sign up for a free trial account at: http://developer.avalara.com/api-get-started

For an overview of how AvaTax Calculates tax using our API's visit http://developer.avalara.com/api-docs/designing-your-integration

Samples included are listed below with associated links to documentation:

ValidateRequest.py (http://developer.avalara.com/api-docs/rest/address-validation)

GetTaxRequest.py POST (http://developer.avalara.com/api-docs/rest/tax/post)

GetTaxRequestSerialized.py POST (http://developer.avalara.com/api-docs/rest/tax/post)

CancelTaxRequest.py (http://developer.avalara.com/api-docs/rest/tax/cancel)

Extras:

encode.py is a sample that will convert your account and license key into a base64 string to use as an authKey if desired.

credentials.py  is a safe place to store your account credentials in the form:
development = '110001234:A1B2C3D4E5F6G7'

data.py is a sample GetTaxRequest body that can be imported by GetTaxRequest.py

GetTaxRequestSerialized.py contains a sample json body

Steps to use python samples:

1. Populate Credentials with your development account number and license key in the form [development = 'account:licensekey'] - Note: AvaTax Admin Account username and password can be used alternatively.

2. Validate your destination address using the Validate.py sample. Sample will prompt you for address information.

3. Use the results from Validate.py to populate a GetTaxRequest. 
-- For GetTaxRequest.py modify data.py as required. Left as it is, should return a result from your default AvaTax Organization.
-- For GetTaxRequestSerialized modify the request json data within the sample.

4. The CancelTax.py sample has 4 required fields and is designed to prompt you for the values:
-- CompanyCode is the company that the GetTaxRequest was committed. This field must be populated even if it was a default company code.
-- DocType must be one of the following: SalesInvoice, ReturnInvoice, PurchaseInvoice.
-- DocCode is the Document Code or Invoice number that was used to commit the document.
-- CancelCode must be one of the following: 
--   Unspecified
--   PostFailed
--   DocDeleted
--   DocVoided
--   AdjustmentCancelled
See http://developer.avalara.com/api-docs/api-reference/canceltax for more details

For more information on how to calculate tax using AvaTax API as well as some recommended use cases, visit the Avalara Developer's Network at http://developer.avalara.com/api-docs
