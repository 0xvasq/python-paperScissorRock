
import random, sys

wins = 0
loses = 0
ties = 0

while True:
    print('Lets play rock, paper, scissor')
    print('%s wins, %s loses, %s ties' % (wins, loses, ties))
    print ('press r, p, s')
    try:
        userMove = input("Please enter your choice: ")
        if userMove not in ['r', 'p', 's']:
            raise ValueError('INVALID ENTRY!')
    except ValueError as e:
        print("ERROR, ", e)
        continue
    else:
        break

if userMove == 'r':
    print('You have selected Rock!')
elif userMove == 'p':
    print ('You have selected paper!')
elif userMove == 's':
    print('You have selected Scissora!')

randomNum = random.randint(1,3)

if randomNum == 1:
    compMove = 'r'
    print('Opponent choses Rock')
elif randomNum == 2:
    compMove = 'p'
    print('Opponent selects Paper!')
elif randomNum == 3:
    compMove = 's'
    print('Opponent goes with Scissors')