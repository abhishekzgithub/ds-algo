"""
try tracing this problem to understand it better
coin change

steps:
1.understand combination sum problem
2. get state, array,target,result,index as args
3. keep adding initial ele [1] of coin[1,2,3,4],
 so as to get the "state" to achieve "target"
4. provide stopping condition as to return
"""


def coin_change(state, coin, target,result,index):
    """
    state
    coin
    result
    """
    if sum(state)>target:
        return False
    elif sum(state)==target:
        result.append(state[::])
        return True
    else:
        for ix in range(index,len(coin)):
            state.append(coin[ix])
            coin_change(state,coin,target,result,ix)
            state.pop()
    return result

def coin_change_helper(coin,target):
    coin.sort()
    state=[]
    index=0
    result=[]
    return coin_change(state, coin, target,result,index)


_coin=[4,2,3,1]
_target=8
#_coin=[1,2,5]
#_target=11 #3
print(coin_change_helper(_coin,_target),end="\n")