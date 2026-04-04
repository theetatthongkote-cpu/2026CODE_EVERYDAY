# Day 45 —  JSON pt 2
# Fresh practice file by myself no chat gpt
import json

json_data = """
{   "students": [
    {
        "name":"Tigger",
        "GPA": 3.5,
        "Hobbies": ["Basketball", "Coding", "Reading"]
    },
    {
        "name":"James",
        "GPA": 4.0,
        "Hobbies": ["Football", "Gaming", "Cooking"]
    }
    ]
}
"""
data = json.loads(json_data)


new_json = json.dumps(data, indent=4, sort_keys=True)


with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
print(data["students"][1]["Hobbies"][1])
