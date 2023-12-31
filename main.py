import os
import sys
from dotenv import load_dotenv

import buffapi
import googlesheetapi
import pyfiglet

import ranges


load_dotenv()

print(pyfiglet.figlet_format("BuffToSheet"))

print("Getting inventory data")
inv = buffapi.getinv()

if not inv:
    sys.exit()

print("Google authentication")
creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

print("Getting already added ids")
ids = googlesheetapi.read_num_line(creds, sheetid, ranges.ID_RANGE, int)

if not ids:
    sys.exit()

print('')
print("Inserting inventory")
googlesheetapi.write_inventory(creds, sheetid, inv, ids, ranges.ITEM_RANGE)
