s = [input() for _ in range(206)]
s = [x.replace(x[0:x.index(":") + 2], "").split("|") for x in s]
y = 0
for x in s:
    y += int(2 ** (len(set(x[0].split()).intersection(set(x[1].split()))) - 1))
print(y)
