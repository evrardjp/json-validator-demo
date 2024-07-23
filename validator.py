import json
import jsonschema
from jsonschema import validate
import sys
import os


def main():
    # Load the schema
    with open('golden_rules_audit_schema.json','r') as sf:
        schema = json.load(sf)

    if len(sys.argv) != 2:
        print("Usage: python validate.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]

    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Cannot file find named {file_name}.")
        sys.exit(2)
    except Exception as e:
        print(f"Error: Failed to read or parse JSON file '{file_name}'.")
        print(e)
        sys.exit(1)

    try:
        validate(instance=data, schema=schema)
        print("Sample data is valid")
    except jsonschema.exceptions.ValidationError as err:
        print("Sample data is invalid")
        print(err.message)
        sys.exit(1)

if __name__ == "__main__":
    main()

