import json
import pandas as pd


def parse_gps(value):
    return float(value) if value != 'Unknown' else value


def parse_yes_no(value):
    return True if value == 'Y' else False if value == 'N' else 'Unknown' 


def handle():
    data = []
    filename = 'data/data.xlsx'
    xls = pd.read_excel(filename, sheet_name=None, index_col=None, header=None)
    for sheet_name in xls.keys():
        df = xls[sheet_name]
        link = False
        for idx, row in df.iterrows():
            if not link:
                link = row[0]
            # Some rows don't have the data we need
            # some are empty floats, so we'll skip them
            # some have no gps data
            if type(row[1]) == float or row[3] == 'Unknown':
                continue
            clean_row = {
                'name': sheet_name,
                'year': row[0],
                'name_of_institution_by_location': row[1],
                'name_of_institution': row[2],
                'link': link,
                'latitude': parse_gps(row[3]),
                'longitude': parse_gps(row[4]),
                'institution_type': row[5],
                'native_serving_mission': parse_yes_no(row[6]),
                'abuse_claim': parse_yes_no(row[7])
            }
            data.append(clean_row)

    jsonfile = "data/data.json"
    with open(jsonfile, 'w', encoding='utf-8') as output:
        output.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    handle()