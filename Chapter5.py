# 1. What does the code for an empty dictionary look like?

# Two curly brackets: {}

# 2. What does a dictionary value with a key 'foo' and a value 42 look like?

# {'foo': 42}

# 3. What is the main difference between a dictionary and a list?

# The items stored in a dictionary are unordered, while the items in a list are ordered.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# You will receive a KeyError error

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in
# spam.keys()?

# There is no difference, they both check whether a value exists as a key in the dictionary

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in
# spam.values()?

# 'cat' will return the key 'cat' while spam.values() will return the value for the key 'cat'

# 7. What is a shortcut for the following code?
# if 'color' not in spam:
#     spam['color'] = 'black'

# spam.setdefault('color', 'black')

# 8. What module and function can be used to 'pretty print' dictionary values?

# The prettyprint module and the prettyprint function. pprint.pprint()