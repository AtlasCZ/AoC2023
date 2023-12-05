checkSet = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
inp = [input() for _ in range(1000)]
s = 0
t = [0,0]
for x in inp:
    i = 0
    t[1] = "g"
    for j in range(len(x)):
        if x[j] in checkSet:
            t[i] = x[j]
            i = 1
        elif len(x) - j > 4:
            if x[j:j+5] == "three":
                t[i] = 3
                i = 1
            elif x[j:j+5] == "seven":
                t[i] = 7
                i = 1
            elif x[j:j+5] == "eight":
                t[i] = 8
                i = 1
            elif x[j:j+4] == "four":
                t[i] = 4
                i = 1
            elif x[j:j+4] == "five":
                t[i] = 5
                i = 1
            elif x[j:j+4] == "nine":
                t[i] = 9
                i = 1
            elif x[j:j+3] == "one":
                t[i] = 1
                i = 1
            elif x[j:j+3] == "two":
                t[i] = 2
                i = 1
            elif x[j:j+3] == "six":
                t[i] = 6
                i = 1
            continue
        elif len(x) - j > 3:
            if x[j:j+4] == "four":
                t[i] = 4
                i = 1
            elif x[j:j+4] == "five":
                t[i] = 5
                i = 1
            elif x[j:j+4] == "nine":
                t[i] = 9
                i = 1
            elif x[j:j+3] == "one":
                t[i] = 1
                i = 1
            elif x[j:j+3] == "two":
                t[i] = 2
                i = 1
            elif x[j:j+3] == "six":
                t[i] = 6
                i = 1
            continue
        elif len(x) - j > 2:
            if x[j:j+3] == "one":
                t[i] = 1
                i = 1
            elif x[j:j+3] == "two":
                t[i] = 2
                i = 1
            elif x[j:j+3] == "six":
                t[i] = 6
                i = 1
    if t[1] == "g":
        t[1] = t[0]
    s += 10 * int(t[0]) + int(t[1])
print(s)
