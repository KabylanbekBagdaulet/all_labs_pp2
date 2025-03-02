import os

path= r"c:\Users\bako\OneDrive - АО Казахстанско-Британский Технический Университет\Документы"
if os.path.exists(path):
    all_items = os.listdir(path) 

files = [f for f in all_items if os.path.isfile(os.path.join(path, f))]
directories = [d for d in all_items if os.path.isdir(os.path.join(path, d))]

print("файлы:", files)
print("директории", directories)

