# ======================== what is json ========================
# json is a file format that is used to store and exchange data
# json is a file format that is used to store and exchange data
import json

# ======================== how to use json ========================
# json is a file format that is used to store and exchange data
# json is a file format that is used to store and exchange data
json_data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# json.dumps() is used to convert a Python object into a json string
# json is a file format that is used to store and exchange data
json_data = json.dumps(json_data)
print(json_data)

# ======================== how to read json ========================
# json.loads() is used to convert a json string into a Python object
# json is a file format that is used to store and exchange data
json_data = json.loads(json_data)
print(json_data)
