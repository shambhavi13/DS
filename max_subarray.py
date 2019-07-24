"""
Given a list of number
find the subarray with max sum
"""

def _max_sub_array(nums):

    # intialize at first index
    max_c = max_g = nums[0]

    for i in range(len(nums)-1):
        max_c = max(nums[i], max_c + nums[i])

        if max_c > max_g:
            max_g = max_c

    return max_g


if __name__ == "__main__":
    nums = [1, -2, 4, 3, 1]
    print(_max_sub_array(nums))