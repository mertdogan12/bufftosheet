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


def read_items(creds, sheetid, range_name):
    items_data = get_values(creds, sheetid, range_name)
    items: list[Item] = []

    if not items_data:
        return None

    for item_data in items_data.get("values"):
        if len(item_data) == 0:
            continue

        items.append(Item(
            item_id=item_data[0],
            name=item_data[1],
            new=True if item_data[2] == "yes" else False,
            pic_url=item_data[3],
        ))

    return items


def read_num_line(creds, sheetid, range_name, type: type):
    if type is not float and type is not int:
        raise TypeError

    values = get_values(creds, sheetid, range_name)

    if values == None:
        return None

    lines: list[str] = [value[0] for value in values["values"]]
    prices = [line.replace('¥', '').replace(
        '.', '').replace(',', '.') for line in lines]

    return [type(price) for price in prices]
