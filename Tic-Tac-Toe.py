#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output
def show_board(board):
    clear_output()
    #Designs the board
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# In[ ]:


testboard = [' ']*10
show_board(testboard)


# In[ ]:


def player_marker():
    #Assigns X or O to player
    select_player = input('Select X or O:').upper()
    if select_player == 'X':
        return ('X','O')
    else:
        return ('O','X')


# In[21]:


player_1, player_2 = player_marker()


# In[ ]:


import random
def first_player():
    #who will be player 1
    
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
        


# In[ ]:


def marker_position(board, marker, position):
    board[position] = marker


# In[ ]:


def space_check(board,position):
    
    return board[position] == ' '


# In[13]:


def full_check(board):
    
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[9]:


def win_check(board,marker):
    return((board[7] == marker and board[8] == marker and board[9] == marker) or
           (board[4] == marker and board[5] == marker and board[6] == marker) or
           (board[1] == marker and board[2] == marker and board[3] == marker) or
           
           (board[7] == marker and board[4] == marker and board[1] == marker) or
           (board[8] == marker and board[5] == marker and board[2] == marker) or
           (board[9] == marker and board[6] == marker and board[3] == marker) or
           
           (board[1] == marker and board[5] == marker and board[9] == marker) or
           (board[7] == marker and board[5] == marker and board[3] == marker))


# In[17]:


def marker_placement(board):
    
    position = 0
    
    if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose the position from 1 to 9'))
    return position


# In[24]:


def replay():
    
    return input('Do you want to play again? Select y or n:').lower().startswith('y')


# In[25]:


print('Lets play Tic-Tac-Toe' )

while True:
    
    thisBoard = [' ']*10
    player_1, player_2 = player_marker()
    first_play = first_player()
    
    print(first_play + 'will go first')
    game = input('Do you want to start the game? Select y ot n')
    if game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        
        if first_play == 'Player 1':
            show_board(thisBoard)
            position = marker_placement(thisBoard)
            marker_position(thisBoard, player_1, position )
            if win_check(thisBoard,player_1):
                show_board(thisBoard)
                print('Player 1 is the winner!')
                game_on = False
            else:
                if full_check(thisBoard):
                    show_board(thisBoard)
                    print('This is a Tie!')
                    break
                else:
                    first_play = 'Player 2'        
        
        else:
            show_board(thisBoard)
            position = marker_placement(thisBoard)
            marker_position(thisBoard, player_2, position )
            if win_check(thisBoard,player_2):
                show_board(thisBoard)
                print('Player 2 is the winner!')
                game_on = False
            else:
                if full_check(thisBoard):
                    show_board(thisBoard)
                    print('This is a Tie!')
                    break
                else:
                    first_play = 'Player 1'
    if not replay():
        break


# In[ ]:





# In[ ]:




