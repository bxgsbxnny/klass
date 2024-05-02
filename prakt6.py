# test_dict = {1: 'element 1', 2: 'element 2', 3: 'element 3', 4: 'element 4', 5: 'element 5'}
# print(test_dict)
# keys=test_dict.keys()
# print(keys)
# values=test_dict.values()
# print(values)
# items=test_dict.items()
# print(items)

# test_dict = {'key 1': 'value 1', 'keyyy': 'vlaueee', '123': 123, 'random?': 'yes', 1: 'two'}
# print(test_dict.get('keyyy'),test_dict.get('1'))

# pc = {'info:': 'PC devices', 1: 'Video card', 2: 'Processor', 3: 'Monitor', 4: 'Strawberry', 5: 'Speakers'}
# del pc[4]
# pc[4] = 'Keyboard'
# pc[6] = 'Mouse'
# pc[7] = 'DVD'
# print(pc)

# double_sy = {1: '10111011', 2: '010101', 3: '11111101', 4: '110010', 5: '011010', 6: '100011001'}
# for key in double_sy:
#     a=double_sy.get(key)
#     if key%2==1:
#         print(int(a,2))

dict1={}
while True:
    key1=input("Название книги:")
    value1=input("Автор:")
    if key1=='end' or key1=='всё' or key1=='все':
