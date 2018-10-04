# Practice Questions

# 1. What are the two values of a Boolean data type? How do you write them?
#   True and False

# 2. What are the three Boolean operators?
#   and, or, not

# 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the
# operator and what they evaluate to).
#   True and True = True
#   True and False = False
#   False and True = False
#   False and False = False
#   True or True = True
#   True or False = True
#   False or True = True
#   False or False = False
#   not True = False
#   not False = True

# 4. What do the following expressions evaluate to?
#   (5 > 4) and (3 == 5) : False
#   not (5 > 4) : False
#   (5 > 4) or (3 == 5) : True
#   not ((5 > 4 ) or 3 == 5)) : False
#   (True and True) and (True == False) : False
#   (not False) or (not True) : True

# 5. What are the six comparison operators?
#   <,>,==,!=, <=, >=

# 6. What is the difference between the equal to operator and the assignment operator?
#   Equal to operator compares two values and evaluates to a Boolean. Assignment sets a variable to a specific value

# 7. Explain what a condition is and where you would use one.
#   A condition is an expression used in a flow control statement that evaluates to a Boolean value.

# 8. Identify the three blocks in this code:
#

# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings!
#  if anything else is stored in spam.

# spam = int(input("What is spam?"))
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print('Howdy')
# else:
#     print('Greetings!')

# 10. What can you press if your program is stuck in an infinite loop?
#   Ctrl + c

# 11. What is the difference between break and continue?
#   Break will exit the loop, continue will go back to the beginning of the loop

# 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
#   range(10) will start at 0 and stop once it reaches 10, range(0, 10) will do the same
#   range(0, 10, 1) will do the same but specifies a step argument

# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that
#  prints the numbers 1 to 10 using a while loop.

# for num in range(1, 11):
#     print(num)
#
# i = 1
# while i < 11:
#     print(i)
#     i = i +1

# 14. If you had a function named bacon() inside a module name spam, how would you call it after importing spam?
#  spam.bacon()


