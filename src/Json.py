import json

#If you have a Python object, you can convert it into a JSON string
# by using the json.dumps() method.
#convert json to python

print("convert python into json file")
print("dict: ",json.dumps({"name": "John", "age": 30}))
print("list: ",json.dumps(["apple", "bananas"]))
print("tuple: ",json.dumps(("apple", "bananas")))
print("String: ",json.dumps("hello"))
print("int: ",json.dumps(42))
print("float: ",json.dumps(31.76))
print("bool: ",json.dumps(True))
print("bool: ",json.dumps(False))
print("none: ",json.dumps(None))

