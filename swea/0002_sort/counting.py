my_list = [1, 5, 3, 8, 6, 3, 7, 2, 9, 2, 7, 4, 0]

counter = [0 for i in range(len(my_list))]

for num in my_list:
    counter[num] += 1

# print(counter)

result = []
for value, count in enumerate(counter):
    # print(value, count)

    for i in range(count):
        result.append(value)
print(result)