def make_permutations(x,y,z):
    '''
    takes 3 integer inputs.
    creates as many permutations in the format of
    [x,y,z] and returns the combinations as a list.
    returned format is [[x,y,z],[x,y,z]...]
    '''
    perms = []
    for a in range(0,x+1):
        for b in range(0,y+1):
            for c in range(0,z+1):
                perms.append([a,b,c])
    return perms

def not_sum(perms, n):
    '''
    takes a list and an integer.
    goes through list created by make_permuations(),
    and if x+y+z != n, adds it to a new temp list.
    temporary list created get returned.k
    '''
    not_max = []
    for p in perms:
        if p[0] + p[1] + p[2] != n:
            not_max.append(p)
        
    return not_max

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print(not_sum(make_permutations(x,y,z),n))
