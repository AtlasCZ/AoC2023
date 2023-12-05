s = [input() for _ in range(100)]
s = [x.replace(x[0:x.index(":") + 2], "").split() for x in s]
y = 0
for x in s:
    for i in range(0, len(x), 2):
        a = int(x[i])
        if x[i + 1][0] == "g":
            if a > 13:
                y -= s.index(x) + 1
                break
        elif x[i + 1][0] == "r":
            if a > 12:
                y -= s.index(x) + 1
                break
        else:
            if a > 14:
                y -= s.index(x) + 1
                break
    y += s.index(x) + 1
print(y)
        
                

