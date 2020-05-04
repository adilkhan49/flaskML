import requests

# URL
url = 'http://localhost:5005/api'
url = 'http://25dc6d79.ngrok.io/api'
# Change the value of experience that you want to test
payload = {
	'exp': ['18']
}

r = requests.post(url,json=payload)
# print(r)
print(r.json())