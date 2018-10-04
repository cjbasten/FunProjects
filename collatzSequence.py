def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


number = int(input('Enter a number.'))

if number <= 0:
    print("Number must be greater than 0")
    exit(1)

while number != 1:
    number = collatz(number)
    print(number)