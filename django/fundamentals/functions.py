# print(dir(list))
# print(dir(dict))
lst = [[1, 34],
       [40, 50],
       [5, 70]]
# for ls in lst:
#     for num in ls:
#         if num > 50:
#             print(num)
# print([n for ls in lst for n in ls])
# num_gt = ([n for ls in lst for n in ls if n > 50])
# print(num_gt)

max_num = ([n for ls in lst for n in ls])
print(max(max_num))

max_pair = [ls for ls in lst if max_num in ls]
print(max_pair)

