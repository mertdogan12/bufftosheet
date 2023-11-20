import os
import sys
from dotenv import load_dotenv
import buffapi

import googlesheetapi
import proxies
import ranges


load_dotenv()

proxy_list = proxies.read_proxies()
working_proxies = proxies.test_proxies(proxy_list)

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

items = googlesheetapi.read_items(creds, sheetid, ranges.ITEM_RANGE)
if items is None:
    sys.exit()

prices = buffapi.getitemprices(items, working_proxies)
if prices is None:
    sys.exit()

googlesheetapi.write_current_invvalue(creds, sheetid, prices, ranges.SUM_RANGE)
