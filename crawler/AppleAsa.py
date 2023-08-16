import os
import datetime as dt
from authlib.jose import jwt
from Crypto.PublicKey import ECC
# from crypto.PublicKey import ECC

private_key_file = "D:/work/ASA私钥.pem"
public_key_file = "D:/work/ASA公钥.pem"
client_id = "SEARCHADS.xxxxxxxxxxxxxxx"
team_id = "SEARCHADS.xxxxxxxxxxxxxx"
key_id = "xxxxxxxxxxxxxxxxx"
audience = "https://appleid.apple.com"
alg = "ES256"

# Create the private key if it doesn't already exist.
if os.path.isfile(private_key_file):
    with open(private_key_file, "rt") as file:
        private_key = ECC.import_key(file.read())
else:
    private_key = ECC.generate(curve='P-256')
    with open(private_key_file, 'wt') as file:
        file.write(private_key.export_key(format='PEM'))

# Extract and save the public key.
public_key = private_key.public_key()
if not os.path.isfile(public_key_file):
    with open(public_key_file, 'wt') as file:
        file.write(public_key.export_key(format='PEM'))

# Define the issue timestamp.
issued_at_timestamp = int(dt.datetime.utcnow().timestamp())
# Define the expiration timestamp, which may not exceed 180 days from the issue timestamp.
expiration_timestamp = issued_at_timestamp + 86400*180

# Define the JWT headers.
headers = dict()
headers['alg'] = alg
headers['kid'] = key_id

# Define the JWT payload.
payload = dict()
payload['sub'] = client_id
payload['aud'] = audience
payload['iat'] = issued_at_timestamp
payload['exp'] = expiration_timestamp
payload['iss'] = team_id

# Open the private key.
with open(private_key_file, 'rt') as file:
    private_key = ECC.import_key(file.read())

# Encode the JWT and sign it with the private key.
client_secret = jwt.encode(
    header=headers,
    payload=payload,
    key=private_key.export_key(format='PEM')
).decode('UTF-8')

# Save the client secret to a file.
with open('client_secret.txt', 'w') as output:
     output.write(client_secret)