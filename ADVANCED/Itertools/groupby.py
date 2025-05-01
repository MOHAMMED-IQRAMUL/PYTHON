from itertools import groupby

for key, val in groupby('AAAABBBCCDAA', lambda x: x=='A'):
    print(key, list(val)) 

for key, val in groupby('AAAABBBCCDAA', lambda x: x):
    print(key, list(val))
    
for key, val in groupby({'R1': 19, 'R2': 20, 'R3': 15, 'R4': 14, 'R4': 19 }.items(), lambda x: x[1]>=18):
    print(key, list(val))  