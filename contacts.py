import json

with open('contacts.json') as f:
    contacts = json.load(f)

    for contact in contacts:
        print(f"Name: {contact['name']}, Occupation: {contact['occupation']}")