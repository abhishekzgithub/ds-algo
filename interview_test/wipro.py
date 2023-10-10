word="abhishek"
anagram="hikebash"

from collections import defaultdict

result=defaultdict(list)

def func(nput):
    visited=set()
    for index in range(len(nput)):
        ele ="".join(sorted(nput[index]))
        print(ele)
        for y in range(index,len(nput)):
            anagram_ele="".join(sorted(nput[y]))
            if ele==anagram_ele and (nput[y] not in visited):
                result[nput[index]].append(nput[y])
                visited.add(nput[y])
    print(result.values())

nput = ["ear", "listen", "arm", "are", "silent", "ram", "bear"]
output = [["ear", "are"], ["listen", "silent"], ["ram", "arm"], ["bear"]]

print(func(nput))
