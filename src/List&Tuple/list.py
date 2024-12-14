#list it can store different type of data like int,string,float etc.
marks = [56,98,67,89,90.5,65.5,"shishupal"]

print(marks)
print(type(marks))
print(marks[4])
print(len(marks))

#list slicing
print(marks[1:5])

#list method
list = [23,45,67,87]
list.append(50) # add 50 in last
list.sort()  # sort in asc or desc, it cannot print anythings
list.sort(reverse=True) #sort in desc
list.reverse()
list.insert(2,55)
list.remove(45) 
list.pop()
print(list)

