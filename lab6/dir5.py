list = ["apple", "banana", "cherry"]

with open(r"C:\Users\bako\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\12.txt", "w", encoding = "utf-8") as file:
    file.write(", ".join(list))
    