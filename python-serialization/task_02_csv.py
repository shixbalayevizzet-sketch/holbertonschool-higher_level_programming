#!/usr/bin/env python3
"""
This module provides a function to convert CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file (data.json).

    Args:
        csv_filename (str): The name of the source CSV file.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []

        # Read data from the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data_list.append(row)

        # Write data to the JSON file
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True

    except (FileNotFoundError, IOError, PermissionError):
        return False
