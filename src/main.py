import csv
import json
import sys


def _get_row_from_file(csvfile):
    with open(csvfile) as input:
        for row in csv.DictReader(input.read().split("\n")):
            yield row
        
    
def _get_name(csvfile):
    name = "{}".format(csvfile.replace('data/', '').replace('.csv', '').strip())        
    name_with_spaces = [' ' + char if char.isupper() and idx > 0 else char for idx, char in enumerate(name)]
    return ''.join(name_with_spaces)


def handle(csvfile):
    data = []
    for row in _get_row_from_file(csvfile):
        clean_row = {'name': _get_name(csvfile)}
        for key, value in row.items():
            # make keys lowercase, remove spaces
            key = key.lower().replace(' ', '_').replace('_(y/n)', '')

            # cast lat, lng to float and yes/no into True/False
            value = float(value) if key in ['latitude', 'longitude'] else value
            value = True if value == 'Y' else False if value == 'N' else value  

            # get rid of columns we don't need
            if key not in ['misc', '']:
                clean_row[key] = value
        data.append(clean_row)

    jsonfile = "{}.json".format(csvfile.rstrip('.csv'))
    with open(jsonfile, 'w', encoding='utf-8') as output:
        output.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    handle(sys.argv[1])