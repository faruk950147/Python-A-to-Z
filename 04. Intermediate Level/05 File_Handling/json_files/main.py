# ======================== what is json ========================
# JSON is a file format that is used to store and exchange data
import json

# dumps() is used to convert a Python object into a JSON string
# dump()  is used to convert a Python object into a JSON file
# load()  is used to convert a JSON file into a Python object
# loads() is used to convert a JSON string into a Python object

# ======================== how to dumps ========================
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# json.dumps() → Python object → JSON string
json_string = json.dumps(json_data)
print("JSON String:", json_string)

# ======================== how to dump ========================
# json.dump() → Python object → JSON file
with open("data.json", "w") as f:
    json.dump(json_data, f, indent=4)
print("JSON file created successfully!")

# ======================== how to loads ========================
# json.loads() → JSON string → Python object
python_object = json.loads(json_string)
print("Python Object (from string):", python_object)

# ======================== how to load ========================
# json.load() → JSON file → Python object
with open("data.json", "r") as f:
    loaded_data = json.load(f)
print("Python Object (from file):", loaded_data)
