x = 648363773
y = 74737728
n = 5
MOD = 10**n

def exp(base,pow):
    result = 1
    while pow > 0:
        if pow % 2 == 1:
            result = (result * base) % MOD
        pow = pow // 2
        base = (base * base) %MOD
    return result

print(exp(x,y))