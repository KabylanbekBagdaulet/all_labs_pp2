source = "source.txt"
distanation = "copy.txt"
with open(source, "r", encoding="utf-8") as src, open(distanation, "w", encoding="utf-8") as dis:
    dis.write(src.read())