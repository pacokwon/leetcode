# Two Sum

def twoSum(nums, target):
    length = len(nums)
    nums = list(enumerate(nums))

    nums.sort(key=lambda x: x[1])

    left, right = 0, length - 1
    while left < right:
        sum = nums[left][1] + nums[right][1]
        if sum == target:
            li = nums[left][0]
            ri = nums[right][0]
            return [li, ri] if li < ri else [ri, li]
        elif sum < target:
            left += 1
        else:
            right -= 1

    # error!
    return []

if __name__ == "__main__":
    print(twoSum([15, 11, 7, 2], 9))
