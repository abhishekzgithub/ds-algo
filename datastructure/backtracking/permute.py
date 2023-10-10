
def _permute(backtrack_state,index,num,result,visited):
    if len(backtrack_state)==len(num):
        result.append(backtrack_state[::])
        return True
    if len(backtrack_state)>len(num):
        return False
    for ix in range(index,len(num)):
        if ix not in visited:
            backtrack_state.append(num[ix])
            visited.append(ix)
            _permute(backtrack_state,ix,num,result,visited)
            visited.pop()
            backtrack_state.pop()
    return False

def permute(num):
    backtrack_state=[];result=[]
    #for index in range(len(num)):
    _permute(backtrack_state,0,num,result,visited=[])
    return result

print(permute([1,2,3])) #unfinished