import os
import sys
from dotenv import load_dotenv

import buffapi
import googlesheetapi


load_dotenv()

inv = buffapi.getinv()

if inv is None:
    sys.exit()

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

googlesheetapi.write_inventory(creds, sheetid, inv)
