first = 5
second = 6
f = second - first

for i in range(1,10):
    print(f)
    first = second
    second = f
    f = second - first