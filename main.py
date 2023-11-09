import os
from dotenv import load_dotenv

import buffapi
import googlesheetapi


load_dotenv()

inv = buffapi.getinv()

if inv == None:
    raise

creds = googlesheetapi.auth()
sheetid = os.getenv("SHEETID")

googlesheetapi.write_inventory(creds, sheetid, inv)
