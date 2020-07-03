field_size = eval(input('Please Enter HOw big Your Sea Will Be'))
player_1_field = None
player_2_field = None
player_1_move = None
player_2_move = None


def aim_shoot(player_name, players_move, opp_player_feild):
    aim_x = eval(input('{} Please Enter where you would like to shoot your mighty cannon on your x coordinate'
                       .format(player_name)))
    aim_y = eval(input('{} Please Enter where you would like to shoot your mighty cannon on your y coordinate'
                       .format(player_name)))

    if opp_player_feild[aim_y][aim_x] == '0':
        players_move[aim_y][ aim_x] = '@'
        opp_player_feild[aim_y][aim_x] = '@'

    else:
        players_move[aim_y][aim_x] = '*'
        opp_player_feild[aim_y][aim_x] = '*'
    return opp_player_feild, players_move


def generate_emtpy_field(field_size):
    temp_row = []
    temp_field = []
    for i in range(field_size):
        for j in range(field_size):
            temp_row.append(' ')

        temp_field.append(temp_row)
        temp_row = []
    return temp_field


def check_if_still_has_ships(normal_player_field):
    numships = 0
    for(x) in range(field_size):
        for(y) in range(field_size):
            if normal_player_field[x][y] == '0':

                numships += 1

    return numships


def print_field(list_display):

        print(' ',end='|')
        for b in range(field_size):
            if b == field_size - 1:
                print(('{0}'.format(b)), end='|\n')
            else:

                print(('{0}'.format(b)), end='|')

        for i in range(field_size):
            for j in range(field_size):
                if j == 0:
                    print('{0}|{1}'.format(i, list_display[i][j]), end='|')

                elif j == field_size - 1:
                    print(list_display[i][j], end='|\n')

                else:
                    print(list_display[i][j], end='|')


def ship_placement(player_name, player_field):



    for i in range(field_size):
        print_field(player_field)

        x_move = eval(input('{0} please enter where your x coordinate for you battle ship!'.format(player_name)))

        y_move = eval(input('{0} please enter where your y coordinate for your battle ship'.format(player_name)))
        if player_field[y_move][x_move] == '0':
            print('EEEk you cant place two ships on one tile they will crash!\n Here Enter a new tile for your ship')
            x_move = eval(input('{0} please enter where your x coordinate for you battle ship!'.format(player_name)))

            y_move = eval(input('{0} please enter where your y coordinate for your battle ship'.format(player_name)))

        player_field[y_move][x_move] = '0'

    return player_field


if  __name__ == "__main__":

    player_1_field = generate_emtpy_field(field_size)

    player_2_field = generate_emtpy_field(field_size)
    player_1_move = generate_emtpy_field(field_size)
    player_2_move = generate_emtpy_field(field_size)
    player_1 = (input('please enter your username player1'))
    player_2 = (input('please enter your username player2'))
    player_1_field = ship_placement(player_1, player_1_field)
    print('\n ' * 100)
    player_2_field = ship_placement(player_2, player_2_field)
    while True:
        print('\n ' * 100)
        time_waster = input('Look away {} and press enter'.format(player_2))

        print('Your opponents field')
        print_field(list_display=player_1_move)
        print('Your field')
        print_field(list_display=player_1_field)
        player_2_field, player_1_move = aim_shoot(player_name=player_1, players_move=player_1_move,
                                                  opp_player_feild=player_2_field)
        print('Your opponents field after shooting')
        print_field(list_display=player_1_move)
        time_waster5 = input(' {} end your turn by pressing enter'.format(player_1))
        num_player_2_ships = generate_emtpy_field(player_2_field)

        if num_player_2_ships == 0:
            print('player 1 is winner')
            time_waster4 = input('Game Over {} all yours ships are sunk and your probably drowning!'.format(player_2))
        print('\n ' * 100)
        time_waster2 = input('Look away {} and press enter'.format(player_1))

        print('Your opponents field')
        print_field(list_display=player_2_move)
        print('Your field')
        print_field(list_display=player_2_field)

        player_1_field, player_2_move = aim_shoot(player_name=player_2, players_move=player_2_move,
                                                  opp_player_feild=player_1_field)
        print('Your opponents field after shooting')
        print_field(list_display=player_2_move)
        time_waster5 = input(' {} end your turn by pressing enter'.format(player_2))
        num_player_1_ships = generate_emtpy_field(player_1_field)
        if num_player_1_ships == 0:

            time_waster4 = input('Game Over {} all yours ships are sunk and your probably drowning!'.format(player_1))
        time_waster3 = input('Look away {} and press enter'.format(player_2))

        print_field(list_display=player_1_field)





