import json


def convertJson(data):
    try:
        with open(data) as json_file:
            return json.load(json_file)
    except TypeError:
        print("Not a json file")
