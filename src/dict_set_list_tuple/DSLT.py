#dictionary - collection of ordered, changeable,not allow duplicate, and have key : value pair
dict = {
    'a':1,
    'name':"shishupal",
    "city":"patna",
    "pin": 804453
}
len(dict)
dict['age'] = 25
dict.pop('age')
dict.popitem()
dict.update({'age':25})
dict.keys()
dict.values()
dict.items()
dict.get('age')
dict.get('name')
dict.get('age',25)
print(type(dict))
print(dict)

#set - collection which is unordered, unchangeable*, and unindexed , duplicate not allow
set = {'a','b','c',2,56,"shishupal"}
set.add(10)
set.remove(2)
set.discard(56)
print(type(set))
print(set)

#list -itme are ordered ,changeable,allow duplicate,list item are in index form []
list = [1,2,3,4,5,6,7,8,9]
list.append(10)
list.remove(2)
list.pop()
list.sort()
list.reverse()
list.insert(2,55)
print(type(list))
print(list)

#tuple -itme are ordered ,unchangeable,allow duplicate
tuple = (1,2,3,4,5,6,7,8,9)
tuple.count(2)
tuple.index(2)
print(type(tuple))
print(tuple)
