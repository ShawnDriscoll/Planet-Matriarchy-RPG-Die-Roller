
import json
import pprint

with open('Planet Matriarchy Characters/Sample Char.tps', 'r') as json_file:
    data = json.load(json_file)

    pprint.pprint(data)
