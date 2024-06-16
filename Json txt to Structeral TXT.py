import json

# The Below which is in {} is the json txt file :🍌🍌🍌
json_data = '''


{
  "ok": true,
  "result": [
    {"update_id": 465730614, "message": {"message_id": 23285, "from": {"id": 6690362261, "is_bot": false, "first_name": "\u0985 \u0986 \u0987 ABC", "last_name": "Rana Universe", "username": "RupamBhai", "language_code": "en"}}},
    {"update_id": 465730615, "message": {"message_id": 23286, "from": {"id": 6690362261, "is_bot": false, "first_name": "\u0985 \u0986 \u0987 ABC", "last_name": "Rana Universe", "username": "RupamBhai", "language_code": "en"}}},
    {"update_id": 465730616, "message": {"message_id": 23287, "from": {"id": 6690362261, "is_bot": false, "first_name": "\u0985 \u0986 \u0987 ABC", "last_name": "Rana Universe", "username": "RupamBhai", "language_code": "en"}}}
  ]
}


'''

# Load and pretty-print the JSON data
parsed_data = json.loads(json_data)
formatted_json = json.dumps(parsed_data, indent=4)

print(formatted_json)


with open('000 Rana Universe.txt', 'w') as file:
    file.write(formatted_json)

print(f"Formatted JSON has been saved to '000 Rana Universe 🍌🍌🍌.txt'")