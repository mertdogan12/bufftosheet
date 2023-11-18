from buffapi.getinventory import Inventory
from googlesheetapi.read import read_ids
from googlesheetapi.write import append_values, update_values
from datetime import datetime


def write_inventory(creds, sheetid, inv: Inventory):
    range_name = "A2:C"
    data = []
    ids = read_ids(creds, sheetid)

    if not ids:
        return None

    for item in inv.items:
        new = "no" if str(item.item_id) in ids else "yes"
        data.append([str(item.item_id), item.name, new])

    update_values(creds, sheetid, range_name, "USER_ENTERED", data)
    print("Inserted successful the inventory data")


def write_current_invvalue(creds, sheetid, item_prices):
    sum = 0
    for price in item_prices:
        sum += price

    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    append_values(creds, sheetid, "F:G", "USER_ENTERED", [[timestamp, sum]])
    print(f"Inserted successful the current inventory value: {item_prices}¥")
