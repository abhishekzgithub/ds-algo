A = [1,6,8,9,10]#n

B=[4,5,6,7,8]#m

result=[]

#o(n)

# for ele in A:
#     if ele in B:
#         result.append(ele)

#a=[1,2,3,...,n-1]
"""
i
i+1 to the left 0
i+1+2 _.right 1
i+1+2+4->left     2 (0+1+2)
i+1+2+4+8-> right   3 (i+0+1+2+3)

k=32->5     right              

input=after 2 jumps
output= right (i+)
find the final position of agent after k jumps

1st jump: +1
2nd jump: -1
3rd jump : 

after k jumps


"""
right=[]
left=[]
k=5
start=0
for i in range(1,k):
    if i%2!=0:
        start+=start+i
    else:
        start-=(start+i)
print(start)


"""
cricket score board
events: runs
input: 0,1(first team ,second) ,run scored(0,1,2,3,4,5,6,-1)
P num of players, O number of overs

class Team:
    team_code:0 or 1
    batsman_queue=[0,1,0,2]

class Player(Team):
    name: 
    bowling:boolean
    batting:boolean
    out:boolean
    sequence:integer

class Bowler(Team):
    name: 
    bowling:boolean
    batting:boolean
    out:boolean
    sequence:integer

class Runs(Team):
    matrix: players x over (runs)
    [[0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0]]

runs=Run()
runs.team_code=0
runs.matrix=P*O


runs.matrix[0][0]=input_run[0]
runs.matrix[0][1]=input_run[1]
runs.matrix[0][5]=input_run[5]
    
runs.matrix[1][0]=input_run[0]


runs.matrix[5][5]=input_run[5]

i,j=row_length,col_length

save
"""