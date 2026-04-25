#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a specified JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file back into a dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
