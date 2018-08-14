import json

jsonStr = '{"name": "cassie", "age":18, "flag": false}'
student = json.loads(jsonStr)
print(type(student))
print(student)

print("\n\n")

#jsonStr1 is an array:数组
jsonStr1 = '[{"name": "cassie", "age":18, "flag": false}, {"name": "cassie", "age":18, "flag": true}]'
student1 = json.loads(jsonStr1)
print(type(student1))
print(student1)

print("\n\n")

student3 = [
    {'name': 'cassie', 'age': 18, 'flag': False},
    {'name': 'cassie', 'age': 18, 'flag': True}
]
jsonStr2 = json.dumps(student3)
print(type(jsonStr2))
print(jsonStr2)
