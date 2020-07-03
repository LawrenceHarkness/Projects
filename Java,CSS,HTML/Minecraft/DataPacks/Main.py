import json
with open('First.json') as json_file:
    data = json.load(json_file)

print(data['display']['parent']['tick']['trigger'])
