import requests
url = 'http://localhost:5000/greetings'
response = requests.get(url)
print(response)
