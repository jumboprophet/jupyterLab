# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Mike
organize his grocery shopping list.
"""

# @TODO: Create a list of groceries
grocery = ['Water','Butter','Eggs','Apples','Cinnamon','Sugar','Milk']




# @TODO: Find the first two items on the list
print(grocery[:2])



# @TODO: Find the last five items on the list
print(grocery[-5:])



# @TODO: Find every other item on the list, starting from the second item
print(grocery[1::2])



# @TODO: Add an element to the end of the list
grocery.append('pot')
print(grocery)




# @TODO: Changes a specified element within the list at the given index
grocery[-1] = 'grass'
print(grocery)



# @TODO: Calculate how many items you have in the list
print(len(grocery))

# find index of a particular item 'Eggs'
print(grocery.index('Eggs'))

# remove 'Eggs' from the list
grocery.remove('Eggs')
print(grocery)

# remove the index 0
grocery.pop(0)
print(grocery)

# remove the last item from the list
grocery.pop(-1)
print(grocery)