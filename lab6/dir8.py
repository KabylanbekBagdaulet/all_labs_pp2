import os
path = r"C:\Users\bako\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\Новая папка (2)\1\2.txt"
if(os.path.exists):
    os.remove(path)
    print("succes delete!")
else:
    print("file no exist")