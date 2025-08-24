import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, 'r') as input_f:
        csv_reader = csv.DictReader(input_f)
        data = [OrderedDict(row) for row in csv_reader]

    with open(OUTPUT_FILENAME, 'w') as output_f:
        json.dump(data, output_f, indent=4)

if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
