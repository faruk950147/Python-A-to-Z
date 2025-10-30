import json

json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
with open("data.json", "w") as f:
    json.dump(json_data, f)
    
with open("data.json", "r") as f:
    json_data = json.load(f)
    print(json_data)
