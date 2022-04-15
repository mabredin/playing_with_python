def fib(n):
    f = [0, 1]
    count = 2
    while count <= n:
        f.append(f[count - 1] + f[count - 2])
        count += 1
    return f[n]


print(fib(0))
print(fib(1))
print(fib(3))
print(fib(5))
print(fib(10))