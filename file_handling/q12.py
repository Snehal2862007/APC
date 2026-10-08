with open("student.txt","r")as file:
    content = file.read()
    words = content.split()
    print("total number of words:", len(words))
    for i in range(0,len(words)):
        print(words)
            