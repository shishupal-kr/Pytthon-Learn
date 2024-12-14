info = {
    "name" : "shishupal" ,
    "age" : 25,
    "topics" : ("dictionary","sets"),
    "language" : ["python", "java", "C","sql"],
    "num" : (12,2,34,56),
    25 : "age",
}

print(type(info))
print(info)
print(info["age"])
print(info["num"])
print(info["topics"])
info["surname"] = ["kumar"] #adding some value
print(info)