"""
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
"""
import collections

def miss_num(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] +=1



