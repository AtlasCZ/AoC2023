s = [input() for _ in range(100)]
s = [x.replace(x[0:x.index(":") + 2], "").split() for x in s]
y, r, g, b = 0, 0, 0, 0
for x in s:
    for i in range(0, len(x), 2):
        a = int(x[i])
        if x[i + 1][0] == "g":
            if a > g:
                g = a
        elif x[i + 1][0] == "r":
            if a > r:
                r = a
        else:
            if a > b:
                b = a
    y += b * r * g
    r, g, b = 0, 0, 0
print(y)
