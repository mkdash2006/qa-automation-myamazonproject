
import json

def jsonhandling(filepath):
    with open(filepath) as data:
        formatedjsondata= json.load(data)
        return formatedjsondata