
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
    

    if userMove == 'r':
        print('You have selected Rock!')
    elif userMove == 'p':
        print ('You have selected paper!')
    elif userMove == 's':
        print('You have selected Scissors!')

    randomNum = random.randint(1,3)

    if randomNum == 1:
        compMove = 'r'
        print('and opponent choses Rock!')
    elif randomNum == 2:
        compMove = 'p'
        print('and opponent selects Paper!')
    elif randomNum == 3:
        compMove = 's'
        print('and opponent goes with Scissors!')

    if userMove == 'r' and compMove == 'r':
        print("so its a tie!")
        ties += 1
    elif userMove == 'r' and compMove == 'p':
        print("so you lose!")
        loses += 1
    elif userMove == 'r' and compMove == 's':
        print("so you win!")
        wins += 1
    elif userMove == 'p' and compMove == 'r':
        print("so you win!")
        wins += 1
    elif userMove == 'p' and compMove == 'p':
        print("so its a tie!")
        ties += 1
    elif userMove == 'p' and compMove == 's':
        print("so you lose!")
        loses += 1
    elif userMove == 's' and compMove == 'r':
        print("so you lose!")
        loses += 1
    elif userMove == 's' and compMove == 'p':
        print("so you win!")
        wins += 1
    elif userMove == 's' and compMove == 's':
        print("so you tie!")
        ties += 1
