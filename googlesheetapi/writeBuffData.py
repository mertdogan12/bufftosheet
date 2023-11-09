from buffapi.getinventory import Inventory
from googlesheetapi.write import update_values


def writeInventory(creds, sheetid, inv: Inventory):
    range_name = "A2:C" + str(inv.items.__len__() + 1)
    data = []

    for item in inv.items:
        data.append([str(item.item_id), item.name,
                    str(item.price).replace('.', ',')])

    update_values(creds, sheetid, range_name, "USER_ENTERED", data)
