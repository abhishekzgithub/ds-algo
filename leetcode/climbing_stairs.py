def climbing_stairs(l):
    if l<=1:
        return 1
    return climbing_stairs(l-1)+climbing_stairs(l-2)

def climbings_stairs_helpers(n):
    return climbing_stairs(n)


print(climbings_stairs_helpers(4))