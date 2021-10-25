
import json
import pprint

with open('Planet Matriarchy Characters/Joms Eno.tps', 'r') as json_file:
    data = json.load(json_file)

    pprint.pprint(data)
