'''
longest palindrome
input : forgeeksskeegfor
ouptut: geeksskeeg

str[i, i+1, .....j-1, j]
substring i+1....j-1
'''

23280666478933

def long_palindrome(word):

    # get length of string
    len_word = len(word)
    # table[i][j] is false if substring
    # word[i.....j] is not palindrome
    # else true
    for y in range(len_word):
        for x in range(len_word):
            table = 0
    # table of substring 1
    max_length = 1
    while i < len_word:
        table[i][i] = True
        i = i+1

    # table of substring length 2
    start = 0
    i = 0
    while i < len_word -1:
        if(word[i] == word[i+1]):
            table[i][i+1] = True
            start = i
            max_length = 2
        i = i+1

    # length greater than 2
    # k is length of substring
    k = 3
    while k <= len_word:
        i = 0
        while i < (len_word - k +1):
            # get the ending index of substring
            j = i + k -1
            if table[i+1][j-1] and word[i] == word[j]:
                table[i][j]=True
                if k > max_length:
                    start = i
                    max_length = k
            i = i+1
        k=k+1
    print("Longest palindrome substring is:")







