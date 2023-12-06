numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
s = [input() for _ in range(140)]
s = ["." + x + "." for x in s]
s.insert(0, ["." for _ in range(142)])
s.append(["." for _ in range(142)])
y = 0
i= 1
while i < len(s) - 1:
    j = 1
    while j < len(s[i]) - 1:
        if s[i][j] == "*":
            b = [0, 0]
            c = 0
            k = i - 1
            while k < i + 2:
                m = j - 1
                while m < j + 2:
                    if s[k][m] in numbers:
                        z = 0
                        while s[k][m - 1] in numbers:
                            m -= 1
                            z += 1
                        m += z
                        while s[k][m + 1] in numbers:
                            m += 1
                            z += 1
                        b[c] = int(s[k][m - z: m + 1])
                        c += 1
                    m += 1
                k += 1
            y += b[0] * b[1]
        j += 1
    i += 1
print(y)
