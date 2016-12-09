#!/usr/bin/env python
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               File Owner - Kartheek Palepu            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # Works only for this site - http://www.bluedarttrackings.in/
# # Requirements
# 1) BeautifulSoup
# 2) sendMail.py from my github

import re
import urllib2
from bs4 import BeautifulSoup
from sendMail import mail

# # Got the url by reading the html code from their submit action
urlString = "http://www.bluedart.com/servlet/RoutingServlet?handler=tnt&action=awbquery&awb=awb&numbers="
Waybill_no = "YOUR_WAYBILL_NO"

# # Scrape through the url
url = urllib2.urlopen(urlString + Waybill_no)
data = url.read();

# # Make it more readable
data = BeautifulSoup(data)

# # Pattern to find the details
pattern = """<tr bgcolor="White" valign="middle"><td align="LEFT" colspan="4"><font face="Verdana" size="1"><b>Waybill No : """ + Waybill_no + """</b></font></td></tr>
<tr bgcolor="WHITE">
<td align="LEFT"><font face="Verdana" size="1">(.*)""" + """</font></td>
<td align="LEFT"><font face="Verdana" size="1">(.*)""" + """</font></td>
<td align="LEFT"><font face="Verdana" size="1">(.*)""" + """</font></td>
<td align="LEFT"><font face="Verdana" size="1">(.*)""" + """</font></td>
</tr>"""

# # Search the pattern
m = re.search(pattern, str(data))

# # Get details into respective variables
status_location = m.group(1)
status_details = m.group(2)
status_date = m.group(3)
status_time = m.group(4)

# # Concatenate them
your_shipment = "Shipment At " + status_location + " and" + status_details + "on " + status_date + " at " + status_time

# # Get a mail
mail("your_email_id", "BLUEDART - WAYBILL NO: " + Waybill_no, your_shipment)


# # # Tried using Mechanize

# from mechanize import Browser
# import mechanize
# # br = Browser()
# Br = Browser(factory=mechanize.RobustFactory())
# Br.open("http://www.bluedarttrackings.in/")
# Br.form = Br.global_form()
# Br.select_form(nr=0)
# Br["number"] = Waybill_no
# response = Br.submit()
# text = response.get_data()
