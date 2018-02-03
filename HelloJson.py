import json
from pprint import pprint

Jobj = json.load(open('Test.json'))
print(open('Test.json').read())
pprint(Jobj)