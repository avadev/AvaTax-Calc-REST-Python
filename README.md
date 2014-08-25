<p>The<strong> AvaTax-Calc-REST-Python </strong>repository is a set of python sample requests that demonstrate the <a href="http://developer.avalara.com/api-docs/rest" target="_blank"><strong>AvaTax REST API</strong></a> methods:
  <a href="http://developer.avalara.com/api-docs/rest/tax/post/" target="_blank"><strong>tax/get POST</strong></a>, <a href="http://developer.avalara.com/api-docs/rest/tax/get" target="_blank"><strong>tax/get GET</strong></a>, <a href="http://developer.avalara.com/api-docs/rest/tax/cancel" target="_blank"><strong>tax/cancel POST</strong></a>, and<a href="http://developer.avalara.com/api-docs/rest/address-validation" target="_blank"><strong> address/validate GET</strong></a>.</p>
<p> For more information on the use of these methods and the AvaTax product, please visit our <strong>Developer's Network </strong>site at <a href="http://developer.avalara.com/" target="_blank">http://developer.avalara.com/</a> or <strong>Avalara's Home </strong>page at <a href="http://www.avalara.com/" target="_blank">http://www.avalara.com/</a></p>
<h4>Dependencies</h4>
<p> Python 2.7 or later </p>
<h4>Requirements</h4>
<p> Authentication requires a <strong>Service URL</strong>, a valid <strong>Account Number</strong> and<strong> License Key</strong>. Samples are coded to use the provided <em>credentials.py</em> sample that you will need to modify with your account information.</p>
<p>If you do not have an AvaTax account, a free trial account can be acquired through our [developer site](http://developer.avalara.com/api-get-started) </p>
<p> Authentication requires a valid <strong>Account Number</strong> and <strong>License Key</strong>, which should be entered in <em>each </em>of the sample requests that you would like to test.</p>
<p>If you do not have an AvaTax account, a free trial account can be acquired through our <a href="http://developer.avalara.com/api-get-started">developer site</a> </p>
<p><strong>Samples Included</strong></p>
<table>
  <tr>
    <td width="176"><div align="center"><strong>API</strong></div></td>
    <td width="628"><div align="center"><strong>Method Demonstrated</strong></div></td>
  </tr>
  <tr>
    <td><strong>credentials.py</strong></td>
    <td>Used for centralizing URL, Account Number and License Key for all API samples.</a>.</td>
  </tr>
  <tr>
    <td><strong>ValidateAddressTest.py</strong></td>
    <td>Demonstrates the <a href="http://developer.avalara.com/api-docs/rest/address-validation">ValidateAddress</a> method to <a href="http://developer.avalara.com/api-docs/api-reference/address-validation">normalize an address</a>.</td>
  </tr>
  <tr>
    <td><strong>EstimateTaxTest.py</strong></td>
    <td>Demonstrates the <a href="http://developer.avalara.com/api-docs/rest/tax/get">EstimateTax</a> method used for product- and line- indifferent tax estimates.</td>
  </tr>
  <tr>
    <td><strong>GetTaxTest.py</strong></td>
    <td>Demonstrates the <a href="http://developer.avalara.com/api-docs/rest/tax/post">GetTax</a> method used for product- and line- specific <a href="http://developer.avalara.com/api-docs/api-reference/gettax">calculation</a>.</td>
  </tr>
  <tr>
    <td><strong>CancelTaxTest.py</strong></td>
    <td>Demonstrates the <a href="http://developer.avalara.com/api-docs/rest/tax/cancel">CancelTax</a> method used to <a href="http://developer.avalara.com/api-docs/api-reference/canceltax">void a document</a>.</td>
  </tr>
  <th colspan="2" align=left><strong>Other Files Included in this Repository</strong></th>
  <tr>
    <td><strong><em>.gitattributes</em></strong></td>
    <td><em>GitHub attribute file. Not required for sample use.</em></td>
  </tr>
  <tr>
    <td><strong><em>.gitignore</em></strong></td>
    <td><em>GitHub config file. Not required for sample use.</em></td>
  </tr>
  <tr>
    <td><strong>LICENSE.md</strong></td>
    <td>Apache License TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION</td>
  </tr>
  <tr>
    <td><strong>README.md</strong></td>
    <td>This document describing how to make use of the sample API code.</td>
  </tr>
</table>
<h4><strong>Resources</strong><br />
</h4>
<p><strong>Developer API Documentation</strong> is located here: <a href="http://developer.avalara.com/api-docs" target="_blank">http://developer.avalara.com/api-docs</a></p>
<p>The <strong>Avalara AvaTax API Reference</strong> is located here: <a href="http://developer.avalara.com/api-docs/avalara-avatax-api-reference" target="_blank">http://developer.avalara.com/api-docs/avalara-avatax-api-reference</a></p>
<p>Find out what other developers are talking about on the <strong><em>Avalara Developer Community Forum</em></strong> located here: <a href="https://community.avalara.com/avalara/category_sets/developers" target="_blank">https://community.avalara.com/avalara/category_sets/developers</a></p>
<p><strong>Frequently Asked Questions</strong> regarding all Avalara products is located here: <a href="https://help.avalara.com/" target="_blank">https://help.avalara.com/</a></p>

