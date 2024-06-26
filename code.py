def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Taking user input
user_input = input("Enter a list of integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Calling the function with user input
print("The input: ", nums)
print("The output: ", singleNumber(nums))
