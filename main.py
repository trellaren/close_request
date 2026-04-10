import hashlib
import requests
import datetime


r = requests.get('https://api.close.com/buildwithus')
print(r.url)
print(r.text)

with open("file.json", "w") as f:
    f.write(r.text)

