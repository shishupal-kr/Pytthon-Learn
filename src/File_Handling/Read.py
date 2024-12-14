"""
Character  Meaning
'r'        open for reading (default)
'w'        open for writing, truncating the file first
'X'        create a new file and open it for writing
'a         open for writing, appending to the end of the file if it exists binary mode
't'        text mode (default)
+          open a disk file for updating (reading and writing)
'b'        binary mode
    open("file.txt","mode")
data = f.read() read all data
data = f.readline() read one line
"""

f = open("spec.txt", "r")
data = f.read()

print(data)
print(type(data))
print(len(data))
f.close()