data = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Doe', 'age': 25},
    {'id': 3, 'first_name': 'Bob', 'last_name': 'Smith', 'age': 40},
]

# Create the mapping
mapping = {'id': 'user_id', 'first_name': 'first_name', 'last_name': 'last_name', 'age': 'age'}

# Iterate over each dictionary in the list and update the keys
for d in data:
    new_d = {}
    for k, v in d.items():
        if k in mapping:
            new_d[mapping[k]] = v
    d.clear()
    d.update(new_d)

print(data)
