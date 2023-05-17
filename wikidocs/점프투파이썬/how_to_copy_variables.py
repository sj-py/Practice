variable1 = 1
copied_variable1 = variable1

print('variable1 =', variable1)
print('copied_variable1 =', copied_variable1)

# even the address of the variables are same if you assign the variable directly
print('address of variable1 =', id(variable1))
print('address of copied_variable1 =', id(copied_variable1))
print('variable1 == copied_variable1 =', id(variable1) is id(copied_variable1))

# how to make different addresses
from copy import copy
copied_variable2 = copy(variable1)
print('variable1 =', variable1)
print('copied_variable2 =', copied_variable2)

print('address of variable1 =', id(variable1))
print('address of copied_variable2 =', id(copied_variable2))
print('variable1 == copied_variable2 =', id(variable1) is id(copied_variable2))

# how to copy the lists
list1 = [1,2,3]
list2 = list1
list3 = list1.copy
list4 = copy(list1)
print(list1, list2, list3, list4)
