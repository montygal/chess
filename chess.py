"""The first thing I need is the names of all the chess board squares.
I'm thinking that they should be put in a list.
The only first move can be pawns.
The user should have the first move and then the computer can have the
second move. The pawns can move one square up or two squares up."""

"""The chess board has a-h and 1-8.
The first player can choose a3/a4 to g3/g4 for the first move.
The computer can pick from a6/a5 to h6/h5 for the first move"""

"""First move options player one:
a3, b3, c3, d3, e3, f3, g3, h3
a4, b4, c4, d4, e4, f4, g4, h4"""

"""First move options for the computer:
a6, b6, c6, d6, e6, f6, g6, h6
a5, b5, c5, d5, e5, f5, g5, h5"""

import random
first_pawn = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
computer_first_pawn = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
pawns_player_one = ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3', 'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4']
pawns_computer = ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5']

#The player's first move. Pick the pawn you want to move.
first_move_input = ''
message = 'Pick the first pawn you want to move.\n'
for index, item in enumerate(first_pawn):
    message += f'{index+1}) {item}\n'
while first_move_input.lower() not in first_pawn:
    first_move_input = input(message)
# print('You are moving pawn:' + '\n' + first_move_input)

#The player's first move. Where are you moving the pawn to?
if first_move_input == 'a2':
    print('You can move your pawn to a3 or a4.')
elif first_move_input == 'b2':
    print('You can move your pawn to b3 or b4.')
elif first_move_input == 'c2':
    print('You can move your pawn to c3 or c4.')
elif first_move_input == 'd2':
    print('You can move your pawn to d3 or d4.')
elif first_move_input == 'e2':
    print('You can move your pawn to e3 or e4.')
elif first_move_input == 'f2':
    print('You can move you pawn to f3 or f4.')
elif first_move_input == 'g2':
    print('You can move your pawn to g3 or g4.')
elif first_move_input == 'h2':
    print('You can move your pawn to h3 or h4.')
else:
    print('Please choose a valid selection.')
choice = input('Where would you like to move your first pawn?')
print(f'You have moved your first pawn to: {choice}')


# moving_to = ''
# message2 = 'Pick the destination of the pawn you want to move.\n'
# for index, item in enumerate(pawns_player_one):
#     message2 += f'{index+1}) {item}\n'
# while moving_to.lower() not in pawns_player_one:
#     moving_to = input(message)
# print('You are moving your pawn to:' + '\n' + moving_to)

#The computer's first move. Pick the pawn you want to move.
# computer_first_move = random.choice(pawns_computer)
# print('The computer has moved the first pawn to:\n' + str(computer_first_move))
