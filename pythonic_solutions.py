import math

def count_nines0(n):
    if n < 10:
        return (n == 9)
    r = [(n // (10 ** i)) %
         10 for i in range(math.floor(math.log(n, 10)), -1, -1)]
    d = r[::-1]
    i, j, k = r[0], sum(
        [d[i] * 10 ** i for i in range(len(r) - 2, -1, -1)]), len(r)
    return (i == 9) * (j + 1) + count_nines0(j) + i * (k - 1) * 10 ** (k - 2)

def count_nines1(n):
    if n < 10:
        return (n == 9)
    s = str(n)
    x, y, l = int(s[0]), int(s[1:]), len(s)
    return (x == 9)*(y+1) + count_nines1(y) + x*(l-1)*10**(l-2)

def count_nines2(n):
    sn = str(n)
    res = 0
    for i, c in enumerate(sn):
        if c == '9':
            res += 1 + (int(sn[i + 1:]) if i < len(sn) - 1 else 0)
        res += (int(sn[:i]) if i > 0 else 0) * 10 ** (len(sn) - i - 1)
    return res
