from collections import defaultdict

dict1 = defaultdict(int)
list1 = ['a', 'b', 'c', 'a', 'b', 'a']
for i in list1:
    dict1[i] += 1
print(dict1)

dict2 = defaultdict(list)
list2 = ['a', 'b', 'c', 'a', 'b', 'a']
for i in list2:
    dict2[i].append(i)
print(dict2)

dict3 = defaultdict(lambda :0)
list3 = ['a', 'b', 'c', 'a', 'b', 'a']
for i in list3:
    dict3[i] += 1
print(dict3)
