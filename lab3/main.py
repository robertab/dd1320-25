from Bintree import Bintree

svenska = Bintree()
engelska = Bintree()
with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
with open("engelska.txt", "r", encoding = "utf-8") as engfil:
    for row in engfil:
        for word in row.split():
            if word in engelska:
                pass
            elif word in svenska:
                engelska.put(word)
                print(word, end=" ")
print("\n")
