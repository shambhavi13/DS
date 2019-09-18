# pair_sum([1,2,2,3] , 4) --> (1,3) (2,2)
def pair_sum(arr, k):
    seen = set()
    output = set()

    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))
    return output

if __name__ == "__main__":
    arr = [1,2,2,3]
    k = 4
    print(pair_sum(arr, k))