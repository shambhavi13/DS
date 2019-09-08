"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Input: [1,2,2,3]
Output: true

Input: [1,3,2]
Output: false

Input: [1,2,4,5]
Output: true
"""
def cmp(a,b):
    return (a>b) - (a<b)


def is_monotonic(A):

    store = 0 # first non zero comparision

    for i in range(len(A)-1):
        # compare curr with next to form
        # stream {-1,0,1}
        # -1:< , 1:>, 0:==
        c = cmp(A[i], A[i+1])
        if c: # not None
            if c != store !=0:
                # return False for zero comparision
                return False
        store = c
    return True

if __name__ == "__main__":
    TEST_1 = [1,2,2,3,0]
    print(is_monotonic(TEST_1))
    TEST_2 = [1,1,1]
    print(is_monotonic(TEST_2))