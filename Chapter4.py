# 1. What is []?

# [] is an empty list

# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume
# spam contains [2, 4, 6, 8, 10]

# spam[2] = 'hello'

# For the following three questions, let's say spam contains the list ['a', 'b', 'c', 'd']

# 3. What does spam[int(int('3' * 2) / 11)] evaluate to?

# 'd', since its looking for the item in index 3

# 4. What does spam[-1] evaluate to?

# The last value, so d

# 5. What does spam[:2] evaluate to?

# ['a', 'b'], it will split from the beginning since no value was chosen and continue up to but not including the
# second value

# For the following three questions, let's say bacon contains the list [3.14, 'cat', 11, 'cat', True].

# 6. What does bacon.index('cat') evaluate to?

# 1

# 7. What does bacon.append(99) make the list value in bacon look like?

# It would add 99 to the end of the list.

# 8. What does bacon.remove('cat') make the list value in bacon look like?

# It will remove the first instance of 'cat' from the list.

# 9. What are the operators for list concatenation and list replication?

# +, *

# 10. What is the difference between the append() and insert() list methods?

# append() will add a value only to the end of a list. insert() can add a value anywhere in a list

# 11. What are two ways to remove values from a list?

# Remove and Del

# 12. Name a few ways that list values are similar to string values?

# Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or
# replicated, and be used witht the in and not in operators.

# 13. What is the difference between lists and tuples?

# Tuples are immutable, you won't be able to change or add values to them

# 14. How do you type the tuple value that has just the integer value 42 in it?

# (42,)

# 15. HOw can you get the tuple form of a list value? How can you get the list form of a tuple value?

# The tuple() and list() functions, respectively

# 16. Variables that "contain" list values don't actually contain lists directly. What do they contain instead?

# The variables will contain a reference to list values

# 17. What is the difference between copy.copy() and copy.deepcopy()?

# Copy will duplicate the list while copy.deepcopy() will duplicate the list and other lists inside the list