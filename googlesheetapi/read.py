from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


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
        print("Got status code %d while reading values in the spreed sheet" %
              error.status_code)
        return None


def read_inv_ids(creds, sheetid):
    ids = get_values(creds, sheetid, "A:A")

    if ids == None:
        return None

    return [id[0] for id in ids["values"][1:]]
