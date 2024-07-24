import pytest
import json
import jsonschema
from jsonschema import validate
import sys
import os

@pytest.fixture(scope='session')
def schema():
    with open('golden_rules_audit_schema.json','r') as sf:
        return json.load(sf)

def test_schema(schema):
    # Test validity of default schema
    try:
        validate(instance={}, schema=schema)
    except jsonschema.exceptions.ValidationError:
        pass

class TestPassing:
    def test_full(self, schema):
        with open('tests/example-pass--full.json', 'r') as f:
            j = json.load(f)
        validate(instance=j, schema=schema)
    
    def test_empty_controls(self, schema):
        with open('tests/example-pass--empty.json', 'r') as f:
            j = json.load(f)
        validate(instance=j, schema=schema)

    def test_backslash(self, schema):
        with open('tests/example-pass--backslash.json', 'r') as f:
            j = json.load(f)
        validate(instance=j, schema=schema)

    def test_asciichars(self, schema):
        with open('tests/example-pass--asciichars.json', 'r') as f:
            j = json.load(f)
        validate(instance=j, schema=schema)

class TestInvalidFiles:
    def test_no_controls(self, schema):
        with open('tests/example-fail--nocontrols.json', 'r') as f:
            j = json.load(f)
        with pytest.raises(jsonschema.exceptions.ValidationError):
            validate(instance=j, schema=schema)

    def test_fail_emptycontrol(self, schema):
        with open('tests/example-fail--emptycontrol.json', 'r') as f:
            j = json.load(f)
        with pytest.raises(jsonschema.exceptions.ValidationError):
            validate(instance=j, schema=schema)

