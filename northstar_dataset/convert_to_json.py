import json
import csv
import os
from pathlib import Path

# without extension
files = [
    "app_events",
    "complaints",
    "drivers",
    "customers",
    "deliveries",
    "hubs",
    "incidents",
    "orders",
    "vehicles"
]

dir = os.path.dirname(__file__)

for file in files:
    data = []

    csv_path = Path(dir + "/" + file + ".csv")
    json_path = Path(dir + "/" + file + ".json")

    with open(csv_path, mode = "r", encoding = "utf-8") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            data.append(row)

    with open(json_path, mode = "w", encoding = "utf-8") as file:
        json.dump(data, file, indent = 4)

    print(f"Converted {file}.csv to json")