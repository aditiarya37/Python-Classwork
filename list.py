doraemonChar = ["Nobita", "Doraemono", "Shizuka"]
print(doraemonChar)
print(doraemonChar[1:3])
print(type(doraemonChar))
print(len(doraemonChar))

shinchanChar = ["Shinchan", "Himawari", "IChan"]

chars = doraemonChar+shinchanChar
print(chars)

doraemonChar.append("Suneo")
print(doraemonChar)
shinchanChar.insert(2,"Kazama")
print(shinchanChar)

doraemonChar.remove("Shizuka")
print(doraemonChar)

shinchanChar.pop()
print(shinchanChar)

shinchanChar.sort(reverse=True)
print(shinchanChar)

del(doraemonChar[0:2])

shinchanChar = doraemonChar.copy()
print(shinchanChar)

shinchanChar.clear()
print(shinchanChar)