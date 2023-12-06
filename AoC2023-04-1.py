s = [input() for _ in range(206)]
print(sum(int(2 ** (len(set(x.replace(x[0:x.index(":") + 2], "").split("|")[0].split()).intersection(set(x.replace(x[0:x.index(":") + 2], "").split("|")[1].split()))) - 1)) for x in s))

