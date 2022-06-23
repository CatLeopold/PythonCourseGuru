import random

set1 = set()
set2 = set()

# print(random.randrange(1,11))
# set2={set.add(random.randrange(1,11)) for i in range(1,11)}
for i in range(1, 11):
    # print(i)
    set1.add(random.randrange(1, 11))
    set2.add(random.randrange(1, 11))
print("set1", set1)
print("set2", set2)
print("объединение", set1.union(set2))
print("разница", set1.difference(set2))
print("пересечение", set1.intersection(set2))
