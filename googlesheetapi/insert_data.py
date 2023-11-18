from buffapi.getinventory import Inventory
from googlesheetapi.write import append_values, update_values
from datetime import datetime


def write_inventory(creds, sheetid, inv: Inventory):
    range_name = "A2:C" + str(inv.items.__len__() + 1)
    data = []

    for item in inv.items:
        data.append([str(item.item_id), item.name,
                    str(item.price).replace('.', ',')])

    update_values(creds, sheetid, range_name, "USER_ENTERED", data)
    print("Inserted successful the inventory data")


def write_current_invvalue(creds, sheetid, item_prices):
    sum = 0
    for price in item_prices:
        sum += price

    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    append_values(creds, sheetid, "F:G", "USER_ENTERED", [[timestamp, sum]])
    print(f"Inserted successful the current inventory value: {item_prices}¥")
