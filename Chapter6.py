# 1. What are escape characters?

# Escape characters represent characters in string values that would otherwise be difficult or impossible to type in
# code.

# 2. What do the \n and \t escape characters represent?

# \n is a new line; \t is a tab.

# 3. How can you put a \ backslash character in a string?

# The \\ escape character will represent a backslash character.

# 4. The string value "Howl's Moving Castle" is a valid string. Why isn't it a problem that the single quote character
# in the word Howl's isn't escaped?

# It is fine since you can use a single quote within double quotes

# 5. If you don't want to put \n in your string, how can you write a string with newlines in it?

# You can use a multiline string with triple quotes.

# 6. What do the following expressions evaluate to?
# 'Hello world!'[1]     This will return the string 'e'
# 'Hello world!'[0:5]   This will return the sliced string of 'Hello'
# 'Hello world!'[:5]    This will return the sliced string of 'Hello'
# 'Hello world!'[3:]    This will return the sliced string of 'lo world!'

# 7. What do the following expressions evaluate to?
# 'Hello'.upper()               This will return 'HELLO'
# 'Hello'.upper().isupper()     This will return True
# 'Hello'.upper().lower()       This will return 'hello'

# 8. What do the following expressions evaluate to?
# 'Remember, remember, the fifth of November.'.split()  This will evaluate to ['Remember,', 'remember,', 'the', 'fifth',
#                                                       'of', 'November.']
# '-'.join('There can be only one.'.split())            This will evaluate to 'There-can-be-only-one.'

# 9. What string methods can you use to right-justify, left-justify, and center a string?
# .rjust(), .ljust(), and .center()

# 10. How can you trim whitespace characters from the beginning or end of a string?
# .lstrip() or rstrip()
