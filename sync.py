import os
import sys
from dotenv import load_dotenv
import buffapi

import googlesheetapi
import proxies


load_dotenv()

proxy_list = proxies.read_proxies()
working_proxies = proxies.test_proxies(proxy_list)

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

ids = googlesheetapi.read_inv_ids(creds, sheetid)
if ids is None:
    sys.exit()

prices = buffapi.getitemprices(ids, working_proxies)
if prices is None:
    sys.exit()

googlesheetapi.write_current_invvalue(creds, sheetid, prices)
