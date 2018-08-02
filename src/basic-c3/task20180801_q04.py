nums = list(range(1,41))

nums_func = lambda x: x % 3 == 0 or x //10 == 3
print(list(filter(nums_func, nums)))
