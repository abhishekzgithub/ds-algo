"""
find all permutation of [1,2,3]
"""

def permute(data, data_list):
    if not data:
        return
    print(data)
    return permute(data[1:], data_list)

def permute_helper():
    data = [1,2,3]
    
    return permute(data[1:], data)

permute_helper()