import requests
with open('dwn.png', 'wb') as file:
    file.write(requests.get('https://blog.bi0s.in/assets/logo.png').content)