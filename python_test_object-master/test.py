"""
このファイルに解答コードを書いてください
"""
import numpy as np

filename = 'input.txt'

with open(filename, 'r') as f:
    list = f.read().splitlines()
    print(list)

m = int(list[-1])
i = []
s = []

for j in range(len(list)-1):
    i.append(int(list[j].split(':')[0]))
    s.append(list[j].split(':')[1])

ans = []
# i_sort = sorted(i)
for j in range(len(list)-1):
    if m % i[j] == 0:
        ans.append(s[j])
        
ans = ''.join(ans)
print(ans)