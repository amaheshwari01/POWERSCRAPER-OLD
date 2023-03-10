import requests
import json
data = {
    'act': '',
    'pw': '',
    'req': 'grades',
}

response = requests.post('http://127.0.0.1:5000/', data=data)
print(response.text)
with open("sample.json", "w") as outfile:
    outfile.write(json.parse(response.text))
