from sheets_auth import auth
#custom inports
from info import *

# INPUT: STRING speadsheet_id, STRING range_name
# RETURNS: LIST all data in range
def count_hours(spreadsheet_id,range_name,ac_watch = False):
    service = auth()
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    rows = result.get('values', [])
    data = {}
    hours_list = getWatchHours(ac_watch)
    counter = 0
    for value in rows:
        if len(value) > 0:
            if value[0] in data:
                data[value[0]] += hours_list[counter]
            else:
                data[value[0]] = hours_list[counter]
        counter +=1
    return data

def print_format(hours_dictionary):
    names_list = hours_dictionary.keys()
    for name in names_list:
        print(name,hours_dictionary[name])

if 1 == 1:
    """
    OPERATOR INSTRUCTIONS (BETA: Updated 20AUG2020)
    1) Set BELOW _spreadsheet_id_ to desired spreadsheet ID from URL IN SINGLE QUOTES.
    2) Verify that BELOW __ac_watch__ variable is correct (True for ACwatch days, False for non).
    2b) (!!!) Ensure that Spreadsheet has data (names) only from E8-E25 .
    3) Set ABOVE to _if 1 == 1:_ to operate. Set to _if 1 == 0:_ when not operating mode.
    4) Open terminal and cd to correct directory.
    5) run with "python3 count_hours.py". Print out should appear on terminal.
    """
    spreadsheet_id = '1UhM2bmBeE2_Ff2yps5ZQTe8vAg6gy5kcn8SzQqoGHgA' # <- ID GOES HERE
    names_dict = count_hours(spreadsheet_id,'E8:E25',ac_watch=True) # <- RANGE PARAM & ACWATCH param
    print_format(names_dict)
