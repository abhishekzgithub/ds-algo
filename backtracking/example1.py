"""
coin change

how to decide when to use for loop-> when doing permuation which is finding all possible values, we use for
Need to focus on splitting the nodes? how

Problem breakdown::
1.print combination of coins 

"""


def coin_change(state, coin, target,index):
    """
    state
    coin
    result
    """
    if not state:
        return 
    if sum(state)==target:
        print(state)
        return True
    if sum(state)>target:
        return False
    if sum(state)<target:
        state.append(coin[index])
        coin_change(state, coin, target, index)
        index+=1
        coin_change(state, coin, target, index)
        index+=1
        coin_change(state, coin, target, index)
        return state

def coin_change_helper(coin,target):
    coin=coin
    result=target
    for c in coin:
        print(coin_change([c], coin, result,index=0))

_coin=[2,3,4]
_target=7
coin_change_helper(_coin,_target)