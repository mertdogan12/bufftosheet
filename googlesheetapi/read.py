from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from buffapi.getinventory import Item


def get_values(creds, spreadsheet_id, range_name):

    try:
        service = build("sheets", "v4", credentials=creds)

        result = (
            service.spreadsheets()
            .values()
            .get(spreadsheetId=spreadsheet_id, range=range_name)
            .execute()
        )

        rows = result.get("values", [])
        print(f"{len(rows)} rows retrieved")
        return result

    except HttpError as error:
        print(
            f"Got status code {error.status_code} while reading values in the spreed sheet")
        return None


def read_items(creds, sheetid):
    items_data = get_values(creds, sheetid, "A2:C")
    items = []

    if not items_data:
        return None

    for item_data in items_data:
        id = item_data[0]
        name = item_data[1]
        new = True if item_data[2] == "yes" else False

        items.append(Item(id, name, new))

    return items

def read_ids(creds, sheetid):
    ids = get_values(creds, sheetid, "A:A")

    if ids == None:
        return None

    return [id[0] for id in ids["values"]]
