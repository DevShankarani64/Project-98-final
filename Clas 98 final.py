Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
    data_a = a.read()

	with open(file2, 'r') as b:
    data_b = b.read()

    with open(file1, 'w') as a:
    a.write(data_b)

    with open(file2, 'w') as b:
    b.write(data_a)

swapFileData()
SyntaxError: expected an indented block after 'with' statement on line 7

def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


with open(file1, 'r') as a:
data_a = a.read()

with open(file2, 'r') as b:
data_b = b.read()

with open(file1, 'w') as a:
a.write(data_b)

with open(file2, 'w') as b:
b.write(data_a)

swapFileData()
SyntaxError: invalid syntax
def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
    data_a = a.read()

    with open(file2, 'r') as b:
    data_b = b.read()

    with open(file1, 'w') as a:
    a.write(data_b)

    with open(file2, 'w') as b:
    b.write(data_a)

swapFileData()
SyntaxError: expected an indented block after 'with' statement on line 6
def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

swapFileData()
SyntaxError: invalid syntax
def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

        
swapFileData()
enter files name:- file1
enter files name:- file2
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    swapFileData()
  File "<pyshell#6>", line 6, in swapFileData
    with open(file1, 'r') as a:
FileNotFoundError: [Errno 2] No such file or directory: 'file1'
f=open("file1.txt","a")
f.write("This is file 1")
f.close()
f=open("file2.txt","a")
f.write("This is file 2")
f.close()
f=open("file1.txt","r")
f.read()

def swapFileData():
    file1 = input("enter files name:- ")
    file2 = input("enter files name:- ")


    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as b:
        b.write(data_a)

        
swapFileData()
SyntaxError: multiple statements found while compiling a single statement
print(f.read())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(f.read())
NameError: name 'f' is not defined
f1=open("file1.text","a")
f1.write("hi")
2
f1.close()
f2=open("file2.txt","a")
f2.write("hello")
5
f2.close()
f1=open("file1.txt","r")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f1=open("file1.txt","r")
FileNotFoundError: [Errno 2] No such file or directory: 'file1.txt'
f3=open("file3.txt","a")
f3.write("hi")
2
f3.close()
f3=open("file3.txt","r")
f3.read()
'hi'
f4=open("file4.txt","a")
f4.write("hello")
5
f4.close()
f4=open("file4.txt","r")
f4.read()
'hello'
def swapFileData():
    file3 = input("enter files name:- ")
    file4 = input("enter files name:- ")


    with open(file3, 'r') as a:
        data_a = a.read()

    with open(file4, 'r') as b:
        data_b = b.read()

    with open(file3, 'w') as a:
        a.write(data_b)

    with open(file4, 'w') as b:
        b.write(data_a)

        
swapFileData()
enter files name:- file3.txt
enter files name:- file4.txt
print(f3.read())
llo
print(f4.read())

f3.read()
''
f4.read()
''
f3=open("file3.txt","r")
f3.read()
'hello'
f4=open("file4.txt","r")
f4.read()
'hi'
