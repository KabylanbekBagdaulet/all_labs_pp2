import os
path = r"c:\Users\bako\OneDrive - АО Казахстанско-Британский Технический Университет\Документы"
if(os.path.exists):
    print("Exist")
    filename = os.path.basename
    directory = os.path.dirname
    print("filename:", filename)
    print("direcname:", directory)
else:
    print("no exist")
