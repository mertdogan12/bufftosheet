import os
import sys
from dotenv import load_dotenv
import buffapi

import googlesheetapi
import proxies
import ranges


load_dotenv()

print("Initializing proxies")
proxy_list = proxies.read_proxies()
working_proxies = proxies.test_proxies(proxy_list)

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

print("")
print("Getting items")
items = googlesheetapi.read_items(creds, sheetid, ranges.ITEM_RANGE)
if not items:
    sys.exit()

print("")
print("Getting sums")
sums = googlesheetapi.read_num_line(creds, sheetid, ranges.SUM_RANGE_PRICE, float)
if not sums:
    sys.exit()

print("")
print("Getting item prices")
prices = buffapi.getitemprices(items, working_proxies)
if not prices:
    sys.exit()

print("")
sum = 0.0
sum_without_new = 0.0

for price in prices:
    if not price.new:
        sum_without_new += price.price

    sum += price.price


googlesheetapi.write_current_invvalue(creds, sheetid, sum, ranges.SUM_RANGE)
googlesheetapi.write_diff(creds, sheetid, sum_without_new, sums[-1], ranges.DIFF)
