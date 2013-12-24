
Typical Results from a validate request:

Address Entered: 
7462+kearny+st   commerce+city co  

The Normalized addess is:
------------------------------
{
	"Address": {
		"County": "Adams",
		"FipsCode": "0800100000",
		"CarrierRoute": "C001",
		"PostNet": "800221335628",
		"AddressType": "S",
		"Line1": "7462 Kearney St",
		"City": "Commerce City",
		"Region": "CO",
		"PostalCode": "80022-1335",
		"Country": "US"
	},
	"ResultCode": "Success"
}

Typical Results from a GetTaxRequest:

{
	"ResultCode": "Success",
	"DocCode": "2013-11-08-1",
	"DocDate": "2013-11-08",
	"Timestamp": "2013-11-11T01:29:44.7705716Z",
	"TotalAmount": "100",
	"TotalDiscount": "0",
	"TotalExemption": "0",
	"TotalTaxable": "100",
	"TotalTax": "4.75",
	"TotalTaxCalculated": "4.75",
	"TaxLines": [{
		"LineNo": "1",
		"TaxCode": "P0000000",
		"Taxability": "true",
		"BoundaryLevel": "Address",
		"Exemption": "0",
		"Discount": "0",
		"Taxable": "100",
		"Rate": "0.047500",
		"Tax": "4.75",
		"TaxCalculated": "4.75",
		"TaxDetails": [{
			"Country": "US",
			"Region": "CO",
			"JurisType": "State",
			"Taxable": "100",
			"Rate": "0.029000",
			"Tax": "2.9",
			"JurisName": "COLORADO",
			"TaxName": "CO STATE TAX"
		},
		{
			"Country": "US",
			"Region": "CO",
			"JurisType": "County",
			"Taxable": "100",
			"Rate": "0.007500",
			"Tax": "0.75",
			"JurisName": "ADAMS",
			"TaxName": "CO COUNTY TAX"
		},
		{
			"Country": "US",
			"Region": "CO",
			"JurisType": "Special",
			"Taxable": "100",
			"Rate": "0.001000",
			"Tax": "0.1",
			"JurisName": "SCIENTIFIC & CULTURAL FAC.(CD)",
			"TaxName": "CO SPECIAL TAX"
		},
		{
			"Country": "US",
			"Region": "CO",
			"JurisType": "Special",
			"Taxable": "100",
			"Rate": "0.010000",
			"Tax": "1",
			"JurisName": "RTD GREATER DENVER",
			"TaxName": "CO SPECIAL TAX"
		}]
	}],
	"TaxAddresses": [{
		"Address": "7562 Kearney St",
		"AddressCode": "2",
		"City": "Commerce City",
		"Country": "US",
		"PostalCode": "80022-1336",
		"Region": "CO",
		"TaxRegionId": "2114686",
		"JurisCode": "0800100000"
	},
	{
		"Address": "435 Ericksen Ave NE # 250",
		"AddressCode": "1",
		"City": "Bainbridge Island",
		"Country": "US",
		"PostalCode": "98110",
		"Region": "WA",
		"TaxRegionId": "0",
		"JurisCode": "5300000000"
	}],
	"TaxDate": "2013-11-08"
}

Typical Results from a CancelTaxRequest:

SUCCESS:

{
"CancelTaxResult": {
"TransactionId": ****************,
"ResultCode": "Success",
"DocId": "28996458"}
}

ERROR:

{
"CancelTaxResult": {
"TransactionId": 4059622600322644,
"ResultCode": "Error",
"Messages": [
{
"Summary": "The tax document could not be found.",
"Details": "34",
"Severity": "Error",
"Source": "Avalara.AvaTax.Services.Tax"}
]
}
}
