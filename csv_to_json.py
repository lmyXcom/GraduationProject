import json
import csv

CSV_FILENAME = 'token_3000imgs.csv'
JSON_FILENAME = 'token_3000imgs.json'
COLUMNS = ('eng', 'id', 'kor')

def convert():
    csv_reader = open(CSV_FILENAME, 'r')
    json_writer = open(JSON_FILENAME, 'w')
    
    services = csv.DictReader(csv_reader, COLUMNS)
    json_writer.write(json.dumps([row for row in services]))


if __name__ == '__main__':
    convert()