numbers = range(1,201)
result = []
for num in numbers:
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))


# print(*result, sep = ',')
print(','.join(result))