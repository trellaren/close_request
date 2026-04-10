import hashlib
import json
import requests
import datetime


r = requests.get('https://api.close.com/buildwithus')
print(r.url)
print(r.text)

with open("file.json", "w") as f:
    f.write(r.text)

data = r.json()
key = data['key'].encode('utf-8')
traits = data['traits']

hashes = [
    hashlib.blake2b(trait.encode('utf-8'), key=key, digest_size=64).hexdigest()
    for trait in traits
]

print(json.dumps(hashes))

post_response = requests.post('https://api.close.com/buildwithus', json=hashes)
print(post_response.status_code)
print(post_response.text)

