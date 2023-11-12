from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def update_values(creds, spreadsheet_id, range_name, value_input_option,
                  _values):
    try:

        service = build('sheets', 'v4', credentials=creds)

        body = {
            'values': _values
        }

        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body
        ).execute()

        print("%s cells updated." % result.get('updatedCells'))

        return result

    except HttpError as error:
        print("Got status code %d while updateing values in the spreed sheet" %
              error.status_code)
        return None


def append_values(creds, spreadsheet_id, range_name, value_input_option, values):
    try:
        service = build("sheets", "v4", credentials=creds)

        body = {"values": values}
        result = (
            service.spreadsheets()
            .values()
            .append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )

        print(f"{(result.get('updates').get('updatedCells'))} cells appended.")
        return result

    except HttpError as error:
        print("Got status code %d while appending values in the spreed sheet" %
              error.status_code)
        return error
