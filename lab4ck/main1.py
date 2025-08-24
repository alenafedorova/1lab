import json

def calculate_sum(input_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    sum_of_products = sum(d['score'] * d['weight'] for d in data)
    return round(sum_of_products, 3)


print(calculate_sum('input.json'))

