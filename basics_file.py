import time
import os
# myfile = open("fruits.txt", "r")open for read
# # print(myfile.read())
# content = myfile.read()
# myfile.close()
# print(content)
# print(content)
#блок with закрывает файл автоматически при выходе из блока
with open("files/fruits.txt") as myfile:
    content = myfile.read()

print(content)

with open("files/vegetables.txt", "w") as myfile:
    myfile.write("mandarine\nonion\napples")

if os.path.exists("files/vegetables.txt"):
    with open("files/vegetables.txt", "a+") as myfile:
        myfile.write("\ntomato")
        myfile.seek(0)#ставим курсор в начало файла
        content = myfile.read()
else:
    print("File is not exist.")
print(content)
time.sleep(5)