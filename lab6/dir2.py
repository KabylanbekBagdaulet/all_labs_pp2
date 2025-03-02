import os
def check(path):
    if not os.path.exists(path):
        print(f"{path} is not exist")
        return
    print(f"{path} is exist")


    print("writiblity:", os.access(path, os.W_OK))
    print("reatiblity:", os.access(path, os.R_OK))
    print("executability:", os.access(path, os.EX_OK))











path= r"c:\Users\bako\OneDrive - АО Казахстанско-Британский Технический Университет\Документы"
check(path)

