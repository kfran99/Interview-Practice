# Given a list of positive integers and a target integer, write a function that returns 
# all of the unique pairs of integers in the list that sum to the target.
# list: [1,2,2,4,6,8,3,5,5]
# target: 10
# return: [(2,8),(4,6),(5,5)]



l = (1, 2, 2, 4, 6, 8, 3, 5, 5)
list2 = (5, -5, 4, 3, 2, 1, -1, -1)


def sum_to_target1(l, n):
    out = []
    for i in range(len(l)-1):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == n:
                out.append((l[i], l[j]))
    return out
# This one takes the 2 twice
print sum_to_target1(l, 10)                


def sum_to_target2(l, n):
    d = {}
    out = []
    for i in l:
        target = n - i
        if d.get(target, 0) > 0:
            out.append((i, target))
            d[target] -= 1
        else:   
            d[i] = d.get(i, 0) + 1
    return out    
# This one works
print sum_to_target2(l, 10)


def sum_to_target3(l, n):
    d = {}
    out = []
    for i in l:
        d[i] = d.get(i, 0) + 1 
    for i in l:
        target = n - i
        if d.get(target) > 0:
            out.append((i, target))
            d[target] -= 1 
    return out
# This one doesn't use the duplicates, but does do the reversal of each
print sum_to_target3(l, 10)