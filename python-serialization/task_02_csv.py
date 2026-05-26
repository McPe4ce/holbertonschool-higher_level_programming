#!/usr/bin/env python3
"""Module that serializes data to JSON and saves it to a file."""

import csv
import json


def serialize_and_save_to_file(data, filename="data.json"):
    """Serializes data into json format"""
    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
    except (IOError, OSError) as e:
        raise FileNotFoundError("Cant write in the file as it doesnt exist")
    except TypeError as e:
        raise TypeError("Data cannot be serialized")


def convert_csv_to_json(filename):
    """Converts the data file from CSV to json file"""
    try:
        with open(filename, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
    except (IOError, OSError):
        raise FileNotFoundError("Cant write in the file as it doesnt exist")
    except TypeError:
        raise TypeError("Data cannot be serialized")
    serialize_and_save_to_file(data, "data.json")
    return True
