import json

data = {
   "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "photography"]
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # indent for pretty printing


with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)
    print(loaded_data['name'])