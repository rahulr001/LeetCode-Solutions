strs = ["cr","car"]

result = ''
for i, a in enumerate(zip(*strs)):
    if len(set(a)) == 1:
        result += a[0]
    elif len(set(a)) > 1:
        break
    else:
        result
print(result)
