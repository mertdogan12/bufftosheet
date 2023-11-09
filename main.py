import os
from dotenv import load_dotenv

import buffapi
from googlesheetapi.auth import auth
from googlesheetapi.writeBuffData import writeInventory


load_dotenv()

inv = buffapi.getinv()

if inv == None:
    raise

creds = auth()
sheetid = os.getenv("SHEETID")

writeInventory(creds, sheetid, inv)
