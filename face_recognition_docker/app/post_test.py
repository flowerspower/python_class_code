import requests
r = requests.post('http://0.0.0.0:5004/',
                  json={"name": "Yuhang", "code_name": "Awesome dad!!! Teacher of this class!!!", "action": "update"})

print r.status_code
print r.json()

# action = requests.post('http://0.0.0.0:5004/', json={"name": "Sean", "action": "delete"})
# print action.status_code
# print action.json()
