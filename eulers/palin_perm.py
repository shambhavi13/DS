'''
Permutation palindrome of a string
chapter 01
Arrays and string
o(n)
time complexity:
'''


def palin_perm(input_str):

    # create a dict
    '''
    |t|2|
    |a|2|
    |c|2|
    |o|1|
    '''
    perms = dict()
    for i in input_str:
        if i in perms:
            perms[i] += 1
        else:
            perms[i] = 1

    odd_count = 0

    for k,v in perms.items():
        if v%2 != 0 and odd_count == 0:
            odd_count += 1
        elif v%2 !=0 and odd_count != 0:
            return False
    return True

# test
print(palin_perm("tacocattio"))




