pl_score = 0
pc_score = 0

def blackjack():
    import random
    from os import system
    import time

    def cls():
        return system('cls')

    cls()

    def pick():
        '''returns a random card from deck'''
        full_deck = ['A', '2', '3', '4', '5', '6',
                     '7', '8', '9', '10', 'J', 'Q', 'K']
        card_chosen = random.choice(full_deck)
        return card_chosen

    player = []
    computer = []
    global pl_score
    global pc_score
    
    player_input = input('Deal first cards?: ').upper()

    if player_input == 'Y':
        print('Deals first card to player and computer')
        player.append(pick())
        computer.append(pick())
        print(f'Your cards: {player} & Computer has{computer}')
        print('computer deals next card')
        player.append(pick())
        computer.append(pick())
        print(f'Your cards are {player}')
        if player == ['A', 'A'] and computer == ['A', 'A']:
            print(f'You both have blackjacks - Draw')
        elif player == ['A', 'A']:
            print('You win with a blackjack')
        elif computer == ['A', 'A']:
            print('You lose, coomputer has black jack')
        else:
            sum_player = 0
            sum_player1 = 0
            sum_player11 = 0
            sum_computer = 0
            sum_computer1 = 0
            sum_computer11 = 0

            for card in player:
                if card == 'A':
                    card = 1
                elif card == 'J' or card == 'Q' or card == 'K':
                    card = 10
                sum_player1 += int(card)
            for card in player:
                if card == 'A':
                    card = 11
                elif card == 'J' or card == 'Q' or card == 'K':
                    card = 10
                sum_player11 += int(card)

            max_player_sum = max(sum_player1, sum_player11)
            min_player_sum = min(sum_player1, sum_player11)
            if max_player_sum <= 21:
                sum_player = max_player_sum
            else:
                sum_player = min_player_sum

            for pc_card in computer:
                if pc_card == 'A':
                    pc_card = 1
                elif pc_card == 'J' or pc_card == 'Q' or pc_card == 'K':
                    pc_card = 10
                sum_computer1 += int(pc_card)
            for pc_card in computer:
                if pc_card == 'A':
                    pc_card = 11
                elif pc_card == 'J' or pc_card == 'Q' or pc_card == 'K':
                    pc_card = 10
                sum_computer11 += int(pc_card)

            max_computer_sum = max(sum_computer1, sum_computer11)
            min_computer_sum = min(sum_computer1, sum_computer11)
            if max_computer_sum <= 21:
                sum_computer = max_computer_sum
            else:
                sum_computer = min_computer_sum

            print(f'Player total is {sum_player}')

            while sum_computer <= 16:
                computer.append(pick())
                sum_computer = 0
                sum_computer1 = 0
                sum_computer11 = 0
                time.sleep(1)  # time in seconds
                print('computer picks a new card')
                for pc_card in computer:
                    if pc_card == 'A':
                        pc_card = 1
                    elif pc_card == 'J' or pc_card == 'Q' or pc_card == 'K':
                        pc_card = 10
                    sum_computer1 += int(pc_card)
                for pc_card in computer:
                    if pc_card == 'A':
                        pc_card = 11
                    elif pc_card == 'J' or pc_card == 'Q' or pc_card == 'K':
                        pc_card = 10
                    sum_computer11 += int(pc_card)
                max_computer_sum = max(sum_computer1, sum_computer11)
                min_computer_sum = min(sum_computer1, sum_computer11)
                if max_computer_sum <= 21:
                    sum_computer = max_computer_sum
                else:
                    sum_computer = min_computer_sum

            deal_again = True
            while deal_again and sum_player < 21:
                deal = input('Do you want another card?: ').upper()
                if deal == 'Y':
                    sum_player = 0
                    sum_player1 = 0
                    sum_player11 = 0
                    player.append(pick())
                    for card in player:
                        if card == 'A':
                            card = 1
                        elif card == 'J' or card == 'Q' or card == 'K':
                            card = 10
                        sum_player1 += int(card)
                    for card in player:
                        if card == 'A':
                            card = 11
                        elif card == 'J' or card == 'Q' or card == 'K':
                            card = 10
                        sum_player11 += int(card)
                    max_player_sum = max(sum_player1, sum_player11)
                    min_player_sum = min(sum_player1, sum_player11)
                    if max_player_sum <= 21:
                        sum_player = max_player_sum
                    else:
                        sum_player = min_player_sum
                    print(player, sum_player)
                else:
                    deal_again = False

            print(
                f'Your cards {player} total {sum_player}\n PC cards {computer} total {sum_computer}')
            if sum_player <= 21 and sum_computer <= 21:
                if sum_player > sum_computer:
                    print('YOU WIN!!!')
                    pl_score += 1
                elif sum_player == sum_computer:
                    print('its a draw, totals are equal')
                    pl_score += 1
                    pc_score += 1
                else:
                    print('yOU lose')
                    pc_score += 1
            elif sum_player > 21 and sum_computer <= 21:
                print('you lose')
                pc_score += 1
            elif sum_player <= 21 and sum_computer > 21:
                print('YOU WIN!!!')
                pl_score += 1
            else:
                print('Its a draw')
                pl_score += 1
                pc_score += 1
# --------------------------------------
        print(f'Player: {pl_score} Computer: {pc_score}')
        cont = input('Do you want to play again?: ').upper()
        if cont == 'Y':
            blackjack()
        else:
            pass
            print('Thank you for playing BlackJack')
            print(f'Player: {pl_score} Computer: {pc_score}')
    else:
        pass


blackjack()
