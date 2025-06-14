import json

slovar= {"name": "Alice", "age": 25}

with open('data.json','w') as f:
    json.dump(slovar, f)

with open('data.json','r') as f:
    print(f.read())

