with open("madlib.txt") as hello:
    newmadlib = hello.read()

with open("newmadlib.txt", 'a') as new:
        new.write(newmadlib + '\n\n')


