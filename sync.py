import os
import sys
from dotenv import load_dotenv
import buffapi
import signal

import googlesheetapi
import proxy


load_dotenv()

proxies = proxy.read_proxies()
print(proxy.test_proxies(proxies))

# creds = googlesheetapi.auth()
# sheetid = os.getenv("SHEETID")
#
# ids = googlesheetapi.read_inv_ids(creds, sheetid)
# if ids is None:
#     sys.exit()
#
# prices = buffapi.getitemprices(ids)
# if prices is None:
#     sys.exit()
#
# googlesheetapi.write_current_invvalue(creds, sheetid, prices)
