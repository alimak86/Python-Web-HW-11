import json
import requests

data = {
  "firstname": "alisa",
  "secondname": "makusheva",
  "email": "nikita@gmail.com",
  "dateofbirth": "1986/06/28",
  "phonenumber": "+16478619006"
}

headers = {'Content-type': 'application/json'}

# response = requests.put('http://127.0.0.1:8000/api/contacts/1',
#                         data=json.dumps(data))
response = requests.get('http://127.0.0.1:8000/api/contacts')
print(response.text)

response = requests.get('http://127.0.0.1:8000/api/contacts/1')
print(response.text)

response = requests.get('http://127.0.0.1:8000/api/contacts/name/kolia')
print(response.text)

response = requests.get('http://127.0.0.1:8000/api/contacts/secondname/putin')
print(response.text)

response = requests.get('http://127.0.0.1:8000/api/contacts/email/nikita@gmail.com')
print(response.text)



#response = requests.delete('http://127.0.0.1:8000/api/contacts/2')
#response = requests.get('http://127.0.0.1:8000/api/contacts/1')

