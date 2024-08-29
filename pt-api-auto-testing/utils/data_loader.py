import json
import csv
import yaml

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
