import os
import sys
from dotenv import load_dotenv

import buffapi
import googlesheetapi
import pyfiglet


load_dotenv()

print(pyfiglet.figlet_format("BuffToSheet"))

print("Getting inventory data")
inv = buffapi.getinv()

if not inv:
    sys.exit()

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

print('')
print("Getting already saved items")
ids = googlesheetapi.read_ids(creds, sheetid)

if not ids:
    sys.exit()

print('')
print("Inserting inventory")
googlesheetapi.write_inventory(creds, sheetid, inv, ids)
