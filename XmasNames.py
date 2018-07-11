import random
from random import randint
list1 = ["Z","B","C", "Cali", "T", "J", "Mike", "Mich" , "Gma"]
list2 = ["Z","B","C", "Cali", "T", "J", "Mike", "Mich" , "Gma"]

#sort list 1
list1 .sort()
print(list1)

#randomize names2
random.shuffle(list2)
shuffle2 = list2
print(shuffle2)

for i in list1:
    j = randint(1,9)
    for j in list2:
        if (i == "T" and j == "J"):
            break
        if (i == "Z" and j == "Cali"):
            break
        if (i == "Mike" and j == "Mich"):
            break
        if i != j:
            print(i, "=", j)
            list2.remove(j)
            break
