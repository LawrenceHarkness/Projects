
player1_score = eval(input('Please enter player 1 score '))
player2_score = eval(input('Please enter player 2 score '))

win_actual_score_player = None
losing_actual_score_player = None

win_actual_score = None
losing_actual_score = None

if player1_score > player2_score:
   win_actual_score = player1_score
   win_actual_score_player = 'Player_1'
   losing_actual_score = player2_score
   losing_actual_score_player = 'Player_2'
elif player1_score < player2_score:
   win_actual_score = player2_score
   win_actual_score_player = 'Player_2'
   losing_actual_score = player1_score
   losing_actual_score_player = 'Player_1'


multiplier = 11 / win_actual_score
estimated_losing_score = round(losing_actual_score * multiplier)
estimated_winning_score = round(win_actual_score * multiplier)


print('|{0}| \t |{1}| \n|{2}| \t |{3}|'.format(win_actual_score_player, losing_actual_score_player,round(estimated_winning_score), round(estimated_losing_score)))


