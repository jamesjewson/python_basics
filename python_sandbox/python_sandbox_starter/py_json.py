# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "Age": 30}'

# Parse to Dictionary
user = json.loads(userJSON)


# print(user)
# print(user['first_name'])


# Dictionary to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car)

print(carJSON)