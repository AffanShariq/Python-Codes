print('Hello World')
game=input('Enter the number of the player')
game=int(game)
number=input ('Enter the number of second player')
number=int (number)  
if game > number:
    print('player 1 Wins') 
elif number > game:
    print('player 2 Wins')
else:
    print ('It is a tie')  