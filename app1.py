import json

student = {
    "name": "Suzuki",
    "age": 15,
    "gender": "male"
}

student_json = json.dumps(student)

print(student)
print(type(student))
print(student_json)
print(type(student_json))