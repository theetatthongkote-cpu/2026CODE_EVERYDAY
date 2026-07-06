# day 120
# two sum using two pointers
def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left + 1, right + 1]
        elif current < target:
            left += 1
        elif current > target:
            right -= 1


nums = [1, 3, 4, 5, 7]
target = 8
print(twoSum(nums, target))
