import os
# file=open('new_file.txt', 'w')
# print("file created successfully")
# file.write("name:snehal ranjeet dalavi \n rollno:10 div=A")
# file.close()
# file=open('new_file.txt', 'r')
# # print(file.read())
# a=file.readline()
# # b=file.readlines()
# print(a)
# # print(b)
# # file.close()

# with open("snehal.txt","w") as a:
#     print("file created successfully")
#     a.write("name:snehal ranjeet dalavi \n rollno:10 div=A")
#     print("written succesufully")

# with open("snehal.txt","r+") as a:
#     print("file opened successfully")
#     a.write("\n name:snehal ranjeet dalavi \n rollno:10 div=A")
#     print("written succesufully")
#     print("file readed successfully")


# with open("snehal.txt","rb+") as a:
#     print("file opened successfully")
#     print(a.read() )
#     print("file readed successfully")


# with open("snehal.txt","r") as a:
#     b=a.readline()
#     print(b)
#     print("readed line succesufully")
#     c=a.readlines()
#     print(c)
#     print("file readed lines succesufully")


# with open("snehal.txt","wb+") as a:
#     print("file opened successfully")
#     a.write(b"hello i am snehal")
#     print("written succesufully")
# file=open("snehal.txt", "r")
# print(file.read() )
# print("file readed successfully")
# file.close()

# file=open("snehal.txt", "w")
# print(file.tell())
# file.write("hi i am snehal")
# file=open("snehal.txt","a")
# file.write("This is an appended line.")
# file=open("snehal.txt", "r")
# file.seek(5)
# print(file.read())
# print(file.tell())
# file.close()

# with open("new_file.txt", "r") as a:
#     with open("snehal.txt", "w") as b:
#         for line in a:
#             b.write(line)
# print("File copied successfully!")
# with open("snehal.txt","r")as a:
#     print(a.readlines())

# with open("empty.txt","x"):
#     print("file created successfully")

with open("empty.txt","r") as a:
    a.unlink("empty.txt")

