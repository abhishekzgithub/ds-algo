"""
https://www.codingninjas.com/studio/problems/find-the-number-of-states_1377943?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
Find the Number of Provinces
n = 3, roads = [ [1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1] 
So, there are '3' provinces.
"""

def find_parent(parent,x):
    if parent[x]==x:
        return x
    return find_parent(parent,parent[x])

def do_union(parent,rank,x,y):
    par_x=find_parent(parent,x)
    par_y=find_parent(parent,y)
    if rank[par_x]>rank[par_y]:
        parent[par_y]=par_x
    elif rank[par_x]<rank[par_y]:
        parent[par_y]=par_y
    else:
        parent[par_y]=par_x
        rank[par_x]+=1
    return rank,parent

def findNumOfProvinces(roads, n):
    # Write your code here
    connected=n
    parent=[]
    rank=[]
    for ix in range(n):
        parent.append(ix)
        rank.append(0)
    
    for col in range(len(roads)):
        for row in range(len(roads[0])):
            if roads[col][row]==1 and find_parent(parent,col)!=find_parent(parent,row):
                connected-=1
                do_union(parent,rank,row,col) # its required

    return connected
n = 3; #3
roads = [ [1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1] ]
roads = [   [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1] ]#2

print(findNumOfProvinces(roads,n))