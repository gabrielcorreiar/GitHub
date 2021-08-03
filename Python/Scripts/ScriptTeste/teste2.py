def method_name(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = 15
values = []
for i in method_name(n):
    values.append(str(i))
print(",".join(values))