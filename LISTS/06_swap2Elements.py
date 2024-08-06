nums = [1,2,3,4,5]
index1 = int(input("Enter the first index: "))
index2 = int(input("Enter the second index: "))
temp = nums[index1]
nums[index1] = nums[index2]
nums[index2] = temp
print(nums)