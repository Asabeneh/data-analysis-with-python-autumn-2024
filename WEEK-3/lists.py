# list: is a collection of items
# items arr indeded and ordered
# List can mutated 

empty_list = list()

print(len(empty_list), empty_list)
print(type(empty_list))
print(dir(empty_list))
lst_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

nums = [1, 2, 3, 4, 5]
copy_lst = nums.copy()
print(nums, len(nums))
print(nums[0])
print(nums[1])
print(nums[4])

last_index = len(nums) - 1
print(nums[last_index])
print(nums[-1])
print(nums[1:4])
print(nums[2:])
print(nums[:3])
# del nums[1:4]
# print(nums)
print(nums)

# nums.append(6)
# nums.extend([7,8,9,10])
print(nums)
# nums.pop()
# nums.pop()
# nums.pop(0)
# print(nums)
# del nums[4]
print(nums)
# nums.remove(5)
# nums.remove(3)
print(nums)
nums.insert(3, 333)
print(nums)
nums.insert(6, 'the last item')
print(nums)
countries = ['Finland','Finland','Finland','Denmark','Norway','Finland','Finland','Sweden']
print(countries.count('Finland'))


print(copy_lst)
copy_lst.reverse()
print(copy_lst)

new_num = [25, 20, 10, 3, 5, 0, 24]
# new_num.sort()
# print(new_num)
print(new_num)
print(sorted(new_num, reverse=False))


