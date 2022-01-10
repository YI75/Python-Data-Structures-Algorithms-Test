def odd(n):
    return [i for i in range(1, n) if i % 2 == 1]
h = odd(100)
print(h)
print([i for i in h if i >10])