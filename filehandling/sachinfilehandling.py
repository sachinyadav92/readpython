def readfile():
    file = open("sachin.txt" , "r")
    print(file.read())

def readline1():
     file = open("sachin.txt" , "r")
     print(file.readline())

def read2lines():
     file = open("sachin.txt" , "r")
     print(file.readline(), file.readline())

def addnametolast():
     file = open("sachin.txt" , "a")
     a = input("Enter your name: ")
     file.write(a)
     file.close()

def readletter():
     file = open("sachin.txt" , "r")
     a = int(input("Enter how many letters to read: "))
     print(file.read(a))

def overwrite():
     file = open("sachin.txt" , "w")
     c = input("CAUTION THIS WILL ERASE EVERYTHING AND WRITE WHAT YOU ENTER: ")
     file.write(c)
     file.close()
     
print ('''1 . Read Full File
2. Read 1st Line
3. Read First Two lines
4. Add Name to last
5. Read Some Letters
6. Overwrite the file
7. Exit''')

x = int(input("Enter Your Choice : "))

if  x == 1:
    readfile()

elif x == 2:
    readline1()

elif x == 3:
    read2lines()

elif x == 4:
    addnametolast()

elif x == 5:
    readletter()

elif x == 6:
    overwrite()
    
else:
    exit()
    
