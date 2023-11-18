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

if inv is None:
    sys.exit()

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

googlesheetapi.write_inventory(creds, sheetid, inv)
