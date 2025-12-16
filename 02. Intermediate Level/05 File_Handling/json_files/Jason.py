import json
data = {
    "company_name": "Infosys",
    "Employees": {
        "E101": {
            "Name": "Omar Faruk",
            "Salary": 50000,
            "Bank_name": "Bank of Bangladesh",
            "Account_number": 7882828323,
            "City": "Delhi"
        },
        "E102": {
            "Name": "Farhad",
            "Salary": 60000,
            "Bank_name": "Bank of Bangladesh",
            "Account_number": 7172727372,
            "City": "Delhi"
        },
        "E103": {
            "Name": "Jay",
            "Salary": 30000,
            "Bank_name": "Bank of Bangladesh",
            "Account_number": 2632326232,
            "City": "Delhi"
        }
    }
}

with open("data.json", "w") as f:
    json.dump(data, f)
    
with open("data.json", "r") as f:
    data = json.load(f)
    # for key in data:
    #     print(data[key])
    for key in data['Employees']:
        # print(data['Employees'][key])
        if data['Employees'][key]['Bank_name'] == "Bank of Bangladesh":
            print("PROCESSING")
            print(f"Salary of {data['Employees'][key]['Name']} is {data['Employees'][key]['Salary']}")
        else:
            print("NOT PROCESSING")
            print(f"Salary of {data['Employees'][key]['Name']} is {data['Employees'][key]['Salary']}")