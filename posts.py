import json
import requests

data = {
  "firstname": "alisa",
  "secondname": "makusheva",
  "email": "alisamakusheva15@gmail.com",
  "dateofbirth": "1986/06/28",
  "phonenumber": "+16478619006"
}

data = {
  "firstname": "nikita",
  "secondname": "putin",
  "email": "nikitaputin15@gmail.com",
  "dateofbirth": "1985/12/05",
  "phonenumber": "+16478617006"
}

headers = {'Content-type': 'application/json'}

response = requests.post('http://127.0.0.1:8000/api/contacts',
                         data=json.dumps(data),
                         headers=headers)

print(response.json())
