"""
coin change

how to decide when to use for loop-> when doing permuation which is finding all possible values, we use for
Need to focus on splitting the nodes? how

Problem breakdown::
1.print combination of coins 

"""


def coin_change(state, coin, target,index=0):
    """
    state
    coin
    result
    """
    if not state:
        return 
    if sum(state)==target:
        #print(state)
        return True
    if sum(state)>target:
        return False
    if sum(state)<target:
        #print("Index",index)
        state.append(coin[index])
        #index+=1
        if not coin_change(state, coin, target, index):
            state=[]
        # #index+=1
        # if not coin_change(state, coin, target, index+1):
        #     state=[] 
        # #index+=1
        # if not coin_change(state, coin, target, index+1):
        #     state=[]
        return state

def coin_change_helper(coin,target):
    coin.sort()
    #index=0
    for c in coin:
        print(coin_change([c], coin, target))


_coin=[4,2,3,1]
_target=8
#_coin=[1,2,5]
#_target=11 #3
coin_change_helper(_coin,_target) #incomplete todo