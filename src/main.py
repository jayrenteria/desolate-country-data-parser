import json
import pandas as pd


def parse_gps(value):
    return float(value) if value != 'Unknown' else value


def parse_yes_no(value):
    return True if value == 'Y' else False if value == 'N' else 'Unknown' 


def handle():
    data = []
    filename = 'data/data.xlsx'
    xls = pd.read_excel(filename, sheet_name=None, index_col=None)
    for sheet_name in xls.keys():
        df = xls[sheet_name]
        for idx, row in df.iterrows():
            # Some rows don't have the data we need
            # some are empty floats, so we'll skip them
            # some have no gps data
            if type(row[1]) == float or row[2] == 'Unknown':
                continue
            clean_row = {
                'name': sheet_name,
                'year': row[0],
                'name_of_institution': row[1],
                'latitude': parse_gps(row[2]),
                'longitude': parse_gps(row[3]),
                'institution_type': row[4],
                'native_serving_mission': parse_yes_no(row[5]),
                'abuse_claim': parse_yes_no(row[6])
            }
            data.append(clean_row)

    jsonfile = "data/data.json"
    with open(jsonfile, 'w', encoding='utf-8') as output:
        output.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    handle()