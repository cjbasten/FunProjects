import random, logging


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

guess = ''
while guess not in ('heads', 'tails'):
    toss = random.randint(0, 2)  # 0 is tails, 1 is heads
    logging.debug('Start of while loop' + guess)
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if toss == int(guess):
        logging.debug('Guess = ' + guess + ' Toss = ' + str(toss))
        print('You got it!')
    else:
        logging.debug('Guess = ' + guess + ' Toss = ' + str(toss))
        print('Nope! Guess again!')
        guess = input()
        if toss == int(guess):
            logging.debug('Guess = ' + guess + ' Toss = ' + str(toss))
            print('You got it!')
        else:
            logging.debug('Guess = ' + guess + ' Toss = ' + str(toss))
            print('Nope. You are really bad at this game.')

