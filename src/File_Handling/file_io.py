"""
Character  Meaning
'r'        open for reading (default)
'w'        open for writing, truncating the file first
'X'        create a new file and open it for writing
'a         open for writing, appending to the end of the file if it exists binary mode
't'        text mode (default)
+          open a disk file for updating (reading and writing)
'b'        binary mode
 etc....

    open("file.txt","mode")
data = f.read() read all data
data = f.readline() read one line
"""


# there is two ways of writing
f = open("spec.txt", "r")
data = f.read()
print(data)
f.close()

#or

with open("spec.txt", "r") as f :  #with always close the f
   data =  f.read()
   print(data)


f = open("list.txt","w")
data = f.write("hey shishupal")
print(data)

f = open("list.txt", "a+")
data = f.write("\nadding some line in last of hey shishupal")
print(data)

f = open("list.txt", "a+")
data = f.write("\nRukkhi is here where are you")
print(data)

f = open("list.txt", "r")
data = f.read()

ne=data.replace("shishupal","sh")
print(ne)



