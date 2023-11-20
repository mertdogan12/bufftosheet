from buffapi.getinventory import Inventory
from googlesheetapi.write import append_values, update_values
from datetime import datetime


def write_inventory(creds, sheetid, inv: Inventory, ids: list[int], range_name):
    data = []

    if not ids:
        return None

    for item in inv.items:
        new = "no" if item.item_id in ids else "yes"
        data.append([str(item.item_id), item.name, new])

    update_values(creds, sheetid, range_name, "USER_ENTERED", data)
    print("Inserted successful the inventory data")


def write_current_invvalue(creds, sheetid, sum, range_name):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    append_values(creds, sheetid, range_name, "USER_ENTERED", [[timestamp, sum]])
    print(f"Inserted successful the current inventory value: {sum}¥")

def write_diff(creds, sheetid, current_sum, old_sum, range_name):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    diff = current_sum - old_sum
    
    append_values(creds, sheetid, range_name, "USER_ENTERED", [[timestamp, diff]])
    print(f"Inserted successful the win/lose: {diff}¥")
