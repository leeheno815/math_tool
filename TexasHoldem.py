import random as r
import os
import time


class PokerCard:
    """
    Class of Cards. It stores card's type and number separately.
    """

    def __init__(self, suit, number):
        self.type = suit
        self.number = number
        if number == 'A':
            self.int = 14
        elif number == 'J':
            self.int = 11
        elif number == 'Q':
            self.int = 12
        elif number == 'K':
            self.int = 13
        elif number == '*':
            self.int = 0
        else:
            self.int = int(number)


def print_menu():
    print("=" * 40)
    print()
    print("{:^40}\n".format("1. Start Game "))
    print("{:^40}\n".format("2. How to Play"))
    print("{:^40}\n".format("3. Poker Hand Ranking"))
    print("{:^40}\n".format("4. Quit Game  "))
    print()
    print("=" * 40)
    return input("Select the menu: ")


def how_to_play():
    os.system("cls")
    print("{:=^80}\n".format("HOW TO PLAY"))
    print("Welcome to LEEHENO first poker game!!\n")
    print("  1. Both player and computer starts with $100000.")
    print("  2. One who reaches $0 first loses.")
    print("  3. Player and computer pay $1000 as entrance fee.")
    print("  4. Cards are handed out. Player and computer get 2 cards each.")
    print("  5. Five cards will be face down on the table. This is called community cards.")
    print("  6. Player can bet any amount of money.")
    print("  7. Computer will bet same amount as player.")
    print("  8. Three community card is revealed.")
    print("  9. 6 and 7 is repeated and another community card is revealed.")
    print("  10. 9 is repeated.")
    print("  11. 6 and 7 is repeated and all computer's hand is revealed.")
    print("  12. One who has better hand wins and collects all the money that was bet.\n")
    print("=" * 80)
    os.system("pause")


def select_explanation():
    while True:
        print("Select the number of hand ranking to see the explanation.")
        ans = input("Input (0 to exit): ")
        try:
            ans = int(ans)
        except ValueError:
            poker_hand_ranking()
            print("Please enter an integer.")
            continue
        if 0 <= ans <= 10:
            return ans
        else:
            poker_hand_ranking()
            print("Please enter an integer between 0 and 10.")
            continue


def poker_hand_ranking():
    os.system("cls")
    print("{:=^40}\n".format("RANKING"))
    print("{:^40}".format("1. Royal Straight Flush"))
    print("{:^40}".format("2. Straight Flush"))
    print("{:^40}".format("3. Four of a Kind"))
    print("{:^40}".format("4. Full House"))
    print("{:^40}".format("5. Flush"))
    print("{:^40}".format("6. Straight"))
    print("{:^40}".format("7. Three of a Kind"))
    print("{:^40}".format("8. Two Pair"))
    print("{:^40}".format("9. Pair"))
    print("{:^40}\n".format("10. High Card"))
    print("=" * 40)


def print_explanation(num):
    os.system("cls")
    if num == 1:
        print("=" * 52)
        print("Royal Straight Flush")
        print("A, K, Q, J, 10, all the same suit.")
        print("Possibility: 0.000153907%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♠', '♠', '♠', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('A', 'K', 'Q', 'J', '10'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♠', '♠', '♠', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 2:
        print("=" * 52)
        print("Straight Flush")
        print("Five cards in a sequence, all in the same suit.")
        print("Possibility: 0.001385169%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♠', '♠', '♠', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('8', '7', '6', '5', '4'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♠', '♠', '♠', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 3:
        print("=" * 52)
        print("Four of a Kind")
        print("All four cards of the same rank.")
        print("Possibility: 0.024009603%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('J', 'J', 'J', 'J', '4'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 4:
        print("=" * 52)
        print("Full House")
        print("Three of a kind with a pair.")
        print("Possibility: 0.144057623%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('10', '10', '10', '9', '9'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 5:
        print("=" * 56)
        print("Flush")
        print("Any five cards of the same suit, but not in a sequence.")
        print("Possibility: 0.196540154%")
        print("   ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print("   │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♠', '♠', '♠', '♠'))
        print("   │       │ │       │ │       │ │       │ │       │")
        print("   │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('J', '9', '8', '4', '2'))
        print("   │       │ │       │ │       │ │       │ │       │")
        print("   │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♠', '♠', '♠', '♠'))
        print("   └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 56)
    elif num == 6:
        print("=" * 52)
        print("Straight")
        print("Five cards in a sequence, but not of the same suit.")
        print("Possibility: 0.392464678%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('9', '8', '7', '6', '5'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 7:
        print("=" * 52)
        print("Three of a Kind")
        print("Three cards of the same rank.")
        print("Possibility: 2.112845138%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('7', '7', '7', 'K', '3'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 8:
        print("=" * 52)
        print("Two Pair")
        print("Two different pairs.")
        print("Possibility: 4.75390156%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('4', '4', '3', '3', '10'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 9:
        print("=" * 52)
        print("Pair")
        print("Two cards of the same rank.")
        print("Possibility: 42.256902761%")
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('A', 'A', '8', '4', '7'))
        print(" │       │ │       │ │       │ │       │ │       │")
        print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 52)
    elif num == 10:
        print("=" * 68)
        print("High Card")
        print("When you haven't made any of the hands 1~9, the highest card plays.\n"
              "In the example below, the jack plays as the highest card.")
        print("Possibility: 50.117739403%")
        print("         ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
        print("         │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % ('♠', '♥', '♣', '♦ ', '♠'))
        print("         │       │ │       │ │       │ │       │ │       │")
        print("         │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % ('3', 'J', '8', '4', '2'))
        print("         │       │ │       │ │       │ │       │ │       │")
        print("         │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % ('♠', '♥', '♣', '♦ ', '♠'))
        print("         └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
        print("=" * 68)
    os.system("pause")


def will_you_cont():
    print("Will you play again?\n1) Yes 2) No")
    while True:
        ans = input("Input: ")
        if ans == '1':
            return True
        elif ans == '2':
            return False
        else:
            os.system("cls")
            print("Please enter 1 or 2\n1) Yes 2) No")


def game_state(x):  # community_cards 에서 *이외의 원소의 개수로 게임의 진행도를 판단한다. gst = game state
    if 5 - x == 0:
        gst = "Pre-flop"
    elif 5 - x == 3:
        gst = "Flop"
    elif 5 - x == 4:
        gst = "Turn"
    elif 5 - x == 5:
        gst = "River"
    else:
        gst = "onGoing"
    return gst


def print_screen(player, computer, community):
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print("                ┌───────┐ ┌───────┐")
    print("                │ %s    │ │ %s    │" % (computer[0].type, computer[1].type))
    print("                │       │ │       │")
    print("                │   %2s  │ │   %2s  │" % (computer[0].number, computer[1].number))
    print("                │       │ │       │")
    print("                │     %s│ │     %s│" % (computer[0].type, computer[1].type))
    print("                └───────┘ └───────┘")
    print("{:^51}\n".format("[Computer's Hand]"))
    print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐")
    print(" │ %s    │ │ %s    │ │ %s    │ │ %s    │ │ %s    │" % (community[0].type, community[1].type,
                                                                  community[2].type, community[3].type,
                                                                  community[4].type))
    print(" │       │ │       │ │       │ │       │ │       │")
    print(" │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │ │   %2s  │" % (community[0].number, community[1].number,
                                                                       community[2].number, community[3].number,
                                                                       community[4].number))
    print(" │       │ │       │ │       │ │       │ │       │")
    print(" │     %s│ │     %s│ │     %s│ │     %s│ │     %s│" % (community[0].type, community[1].type,
                                                                  community[2].type, community[3].type,
                                                                  community[4].type))
    print(" └───────┘ └───────┘ └───────┘ └───────┘ └───────┘")
    print("{:^51}\n".format("[Community Card]"))
    print("                ┌───────┐ ┌───────┐")
    print("                │ %s    │ │ %s    │" % (player[0].type, player[1].type))
    print("                │       │ │       │")
    print("                │  %2s   │ │  %2s   │" % (player[0].number, player[1].number))
    print("                │       │ │       │")
    print("                │     %s│ │     %s│" % (player[0].type, player[1].type))
    print("                └───────┘ └───────┘")
    print("{:^51}\n".format('[' + player_name + "'s Hand" + ']'))
    print("=" * 51)


def deal():  # deal out hands
    for i in range(2):
        player_hand.append(cards_temp.pop(cards_temp.index(r.choice(cards_temp))))
        computer_hand.append(cards_temp.pop(cards_temp.index(r.choice(cards_temp))))


def dealing_animation(t):
    for i in range(60, 15, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print('\n' * 8)
        print(" " * i + "┌───────┐")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "│   *   │")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "└───────┘")
        print('\n' * 10)
        print("=" * 51)
        time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 9)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print("\n" * 9)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 10)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 8)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 11)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 7)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 12)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 6)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 13)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 5)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 14)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 4)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 15)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 3)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 16)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 2)
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 17)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    for i in range(60, 15, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print('\n' * 8)
        print(" " * i + "┌───────┐")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "│   *   │")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "└───────┘")
        print('\n')
        print(" " * 16 + "┌───────┐")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│   *   │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "└───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 7)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 2)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 6)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 3)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 5)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 4)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 4)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 5)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 3)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 6)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print('\n' * 2)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 7)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print()
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 9)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 10)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    for i in range(60, 25, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│   *   │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "└───────┘")
        print('\n')
        print(" " * i + "┌───────┐")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "│   *   │")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│   *   │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "└───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 2)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print()
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 3)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 4)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 16 + "┌───────┐ └───────┘")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 5)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 16 + "┌───────┐ │       │")
    print(" " * 16 + "│       │ └───────┘")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 6)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 16 + "┌───────┐ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ └───────┘")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 7)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 16 + "┌───────┐ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ └───────┘")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 8)
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 16 + "┌───────┐ │       │")
    print(" " * 16 + "│       │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │       │")
    print(" " * 16 + "│       │ └───────┘")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 9)
    print(" " * 26 + "┌───────┐")
    print(" " * 16 + "┌───────┐ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │   *   │")
    print(" " * 16 + "│   *   │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ └───────┘")
    print(" " * 16 + "└───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print('\n' * 10)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    for i in range(60, 25, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│   *   │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "│       │")
        print(" " * 16 + "└───────┘")
        print('\n')
        print(" " * i + "┌───────┐")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "│   *   │")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print()
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 2)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘")
    print(" " * 26 + "┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 3)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "└───────┘ ┌───────┐")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 4)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │ ┌───────┐")
    print(" " * 16 + "└───────┘ │       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 5)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │")
    print(" " * 16 + "│       │ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ │       │")
    print(" " * 26 + "│   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 6)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│   *   │ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ │   *   │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 7)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │")
    print(" " * 16 + "│       │ ┌───────┐")
    print(" " * 16 + "│   *   │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │   *   │")
    print(" " * 16 + "└───────┘ │       │")
    print(" " * 26 + "│       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 8)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐")
    print(" " * 16 + "│       │ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │       │")
    print(" " * 16 + "│       │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ │       │")
    print(" " * 26 + "└───────┘")
    print("\n" * 9)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    os.system("cls")
    print('Computer\'s money : $%d' % computer_money)
    print('Your money : $%d' % player_money)
    print("Prize: $%d" % reward)
    print("=" * 51)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print("\n" * 10)
    print(" " * 16 + "┌───────┐ ┌───────┐")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│   *   │ │   *   │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "│       │ │       │")
    print(" " * 16 + "└───────┘ └───────┘")
    print('\n')
    print("=" * 51)
    time.sleep(t)
    for i in range(60, 0, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print(" " * i + "┌───────┐")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "│   *   │")
        print(" " * i + "│       │")
        print(" " * i + "│       │")
        print(" " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    for i in range(50, 0, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print(" ┌───────┐" + " " * i + "┌───────┐")
        print(" │       │" + " " * i + "│       │")
        print(" │       │" + " " * i + "│       │")
        print(" │   *   │" + " " * i + "│   *   │")
        print(" │       │" + " " * i + "│       │")
        print(" │       │" + " " * i + "│       │")
        print(" └───────┘" + " " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    for i in range(40, 0, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print(" ┌───────┐ ┌───────┐" + " " * i + "┌───────┐")
        print(" │       │ │       │" + " " * i + "│       │")
        print(" │       │ │       │" + " " * i + "│       │")
        print(" │   *   │ │   *   │" + " " * i + "│   *   │")
        print(" │       │ │       │" + " " * i + "│       │")
        print(" │       │ │       │" + " " * i + "│       │")
        print(" └───────┘ └───────┘" + " " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    for i in range(30, 0, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print(" ┌───────┐ ┌───────┐ ┌───────┐" + " " * i + "┌───────┐")
        print(" │       │ │       │ │       │" + " " * i + "│       │")
        print(" │       │ │       │ │       │" + " " * i + "│       │")
        print(" │   *   │ │   *   │ │   *   │" + " " * i + "│   *   │")
        print(" │       │ │       │ │       │" + " " * i + "│       │")
        print(" │       │ │       │ │       │" + " " * i + "│       │")
        print(" └───────┘ └───────┘ └───────┘" + " " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    for i in range(20, 0, -1):
        os.system("cls")
        print('Computer\'s money : $%d' % computer_money)
        print('Your money : $%d' % player_money)
        print("Prize: $%d" % reward)
        print("=" * 51)
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print(" ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐" + " " * i + "┌───────┐")
        print(" │       │ │       │ │       │ │       │" + " " * i + "│       │")
        print(" │       │ │       │ │       │ │       │" + " " * i + "│       │")
        print(" │   *   │ │   *   │ │   *   │ │   *   │" + " " * i + "│   *   │")
        print(" │       │ │       │ │       │ │       │" + " " * i + "│       │")
        print(" │       │ │       │ │       │ │       │" + " " * i + "│       │")
        print(" └───────┘ └───────┘ └───────┘ └───────┘" + " " * i + "└───────┘")
        print("\n")
        print(" " * 16 + "┌───────┐ ┌───────┐")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│   *   │ │   *   │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "│       │ │       │")
        print(" " * 16 + "└───────┘ └───────┘")
        print('\n')
        print("=" * 51)
        time.sleep(t)
    time.sleep(0.5)
    print_screen(computer_hand_show, computer_hand_show, community_cards)

def will_you_pay_entry():  # asks use if they will pay entry fee or not
    print("You will have to pay 1000 won to participate.\nWill you participate?\n1) Yes  2) No")
    ans = input()
    while True:
        if ans == '1':
            return True
        elif ans == '2':
            return False
        else:
            print_screen(computer_hand_show, computer_hand_show, community_cards)
            print("You will have to pay 1000 won to participate.\nWill you participate?\n1) Yes  2) No")
            print("Please press either '1' or '2'")
            ans = input()


def will_you_bet():
    print("Will you bet?\n1) Yes 2) No")
    ans = input()
    while True:
        if ans == '1':
            return True
        elif ans == '2':
            return False
        else:
            print_screen(player_hand, computer_hand_show, community_cards)
            print("Will you bet?\n1) Yes 2) No")
            ans = input("Please press either '1' or '2'")


def how_much_will_you_bet():
    while True:
        try:
            bet = int(input("How much will you bet?\nAmount: "))
            if player_money - bet <= 0:
                print_screen(player_hand, computer_hand_show, community_cards)
                print("Your balance becomes less than or equal to 0.\nPlease choose again.")
                continue
            return bet
        except ValueError:
            print_screen(player_hand, computer_hand_show, community_cards)
            print("Please enter an integer.")
            continue


def betting():
    print_screen(player_hand, computer_hand_show, community_cards)
    bet = how_much_will_you_bet()
    global player_money
    global computer_money
    global reward
    player_money -= bet
    computer_money -= bet
    reward += 2 * bet


def is_royal_straight_flush(hand):
    suits = {'♠': [], '♥': [], '♣': [], '♦ ': []}
    for card in hand:
        suits[card.type].append(card.int)
    for suit, card_list in suits.items():
        if len(card_list) >= 5:
            card_list.sort()
            if [10, 11, 12, 13, 14] in card_list:
                return True
            else:
                return False


def is_straight_flush(hand):
    suits = {'♠': [], '♥': [], '♣': [], '♦ ': []}
    for card in hand:
        suits[card.type].append(card.int)
    for suit, card_list in suits.items():
        if len(card_list) >= 5:
            if 14 in card_list:
                card_list[card_list.index(14)] = 1
            card_list.sort()
            for i in range(len(card_list) - 1):
                if card_list[i] + 1 != card_list[i + 1]:
                    return False
            else:
                return True


def is_four_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    for count in counts.values():
        if count == 4:
            return True
    else:
        return False


def is_full_house(hand):
    counts = {}
    cnt_three = 0
    cnt_two = 0
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    for count in counts.values():
        if count >= 3:
            cnt_three += 1
        elif count >= 2:
            cnt_two += 1
    if (cnt_three == 1 and cnt_two > 0) or cnt_three == 2:
        return True
    else:
        return False


def is_flush(hand):
    suits = {}
    for card in hand:
        suits[card.type] = suits.get(card.type, 0) + 1
    for count in suits.values():
        if count == 5:
            return True
    else:
        return False


def is_straight(hand):
    card_list = []
    for card in hand:
        card_list.append(card.int)
    for card in card_list:
        if card == 14:
            card_list.append(1)
    card_list.sort()
    temp = []
    for i in range(len(card_list) - 1):
        if card_list[i] + 1 == card_list[i + 1]:
            temp.append(card_list[i])
            if len(temp) == 4:
                return True
        else:
            temp.clear()
    return False


def is_three_of_a_kind(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    for count in counts.values():
        if count == 3:
            return True
    else:
        return False


def is_two_pair(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    cnt = 0
    for count in counts.values():
        if count == 2:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False


def is_one_pair(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    for count in counts.values():
        if count == 2:
            return True
    else:
        return False


def what_is_high_card(hand):
    card_list = []
    for card in hand:
        card_list.append(card.int)
    card_list.sort(reverse=True)
    return card_list[0]


def what_is_my_hand(hand):
    if is_royal_straight_flush(hand):
        status = 'Royal Straight Flush'
    elif is_straight_flush(hand):
        status = 'Straight Flush'
    elif is_four_of_a_kind(hand):
        status = 'Four of a Kind'
    elif is_full_house(hand):
        status = 'Full House'
    elif is_flush(hand):
        status = 'Flush'
    elif is_straight(hand):
        status = 'Straight'
    elif is_three_of_a_kind(hand):
        status = 'Three of a Kind'
    elif is_two_pair(hand):
        status = 'Two Pair'
    elif is_one_pair(hand):
        status = 'One Pair'
    else:
        status = 'High Card'
    return status


def make_list_with_zero(hand):
    temp = [i - i for i in range(13)]
    for integer in hand:
        temp[integer - 2] = integer
    return temp


def compare(player, computer):
    for i in range(12, -1, -1):
        if player[i] > computer[i]:
            win = "player"
            break
        elif player[i] < computer[i]:
            win = "computer"
            break
    else:
        win = "no one"
    return win


def straight_flush_kicker(hand):
    suits = {'♠': [], '♥': [], '♣': [], '♦ ': []}
    for card in hand:
        suits[card.type].append(card.int)
    for suit, card_list in suits.items():
        if len(card_list) >= 5:
            for card in card_list:
                if card == 14:
                    card_list.append(1)
            card_list.sort()
            temp = []
            for i in range(len(card_list) - 1):
                if card_list[i] + 1 == card_list[i + 1]:
                    temp.append(card_list[i])
                    if len(temp) == 4:
                        temp.append(card_list[i + 1])
                        break
                else:
                    temp.clear()
            if 1 in temp:
                temp[temp.index(1)] = 14
            temp.sort()
            return temp[-1]


def four_of_a_kind_kicker(hand):
    counts = {}
    temp = []
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count != 4]
    temp.sort()
    return make_list_with_zero(temp)


def full_house_kicker_three_of_a_kind(hand):
    counts = {}
    temp = []
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count == 3]
    temp.sort()
    return temp[-1]


def full_house_kicker_two_pair(hand):
    counts = {}
    temp = []
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count ==2]
    temp.sort()
    return make_list_with_zero(temp)


def flush_kicker(hand):
    suits = {}
    for card in hand:
        suits[card.type] = suits.get(card.type, []).append(card.int)
    for card_list in suits.values():
        if len(card_list) == 5:
            card_list.sort()
            return make_list_with_zero(card_list)


def straight_kicker(hand):
    card_list = []
    for card in hand:
        card_list.append(card.int)
    for card in card_list:
        if card == 14:
            card_list.append(1)
    card_list.sort()
    temp = []
    for i in range(len(card_list) - 1):
        if card_list[i] + 1 == card_list[i + 1]:
            temp.append(card_list[i])
            if len(temp) == 4:
                temp.append(card_list[i + 1])
                break
        else:
            temp.clear()
    if 1 in temp:
        temp[temp.index(1)] = 14
    temp.sort()
    return temp[-1]


def three_of_a_kind_rank(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count == 3]
    temp.sort()
    return make_list_with_zero(temp)


def three_of_a_kind_kicker(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count != 3]
    temp.sort()
    return make_list_with_zero(temp)


def pair_rank(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count == 2]
    temp.sort()
    return make_list_with_zero(temp)


def one_and_two_pair_kicker(hand):
    counts = {}
    for card in hand:
        counts[card.int] = counts.get(card.int, 0) + 1
    temp = [rank for rank, count in counts.items() if count != 2]
    temp.sort()
    return make_list_with_zero(temp)


def tied(player, computer):
    win = 'no one'
    if ranks[what_is_my_hand(player)] == 0:
        if what_is_high_card(player) > what_is_high_card(computer):
            win = "player"
        elif what_is_high_card(player) < what_is_high_card(computer):
            win = "computer"
        else:
            win = "no one"
    elif ranks[what_is_my_hand(player)] == 1 or ranks[what_is_my_hand(player)] == 2:
        win = compare(pair_rank(player), pair_rank(computer))
        if win == 'no one':
            win = compare(one_and_two_pair_kicker(player), one_and_two_pair_kicker(computer))
    elif ranks[what_is_my_hand(player)] == 3:
        win = compare(three_of_a_kind_rank(player), three_of_a_kind_rank(computer))
        if win == 'no one':
            win = compare(three_of_a_kind_kicker(player), three_of_a_kind_kicker(computer))
    elif ranks[what_is_my_hand(player)] == 4:
        if straight_kicker(player) > straight_kicker(computer):
            win = "player"
        elif straight_kicker(player) < straight_kicker(computer):
            win = "computer"
        else:
            win = 'no one'
    elif ranks[what_is_my_hand(player)] == 5:
        win = compare(flush_kicker(player), flush_kicker(computer))
    elif ranks[what_is_my_hand(player)] == 6:
        if full_house_kicker_three_of_a_kind(player) > full_house_kicker_three_of_a_kind(computer):
            win = "player"
        elif full_house_kicker_three_of_a_kind(player) < full_house_kicker_three_of_a_kind(computer):
            win = "computer"
        else:
            win = compare(full_house_kicker_two_pair(player), full_house_kicker_two_pair(computer))
    elif ranks[what_is_my_hand(player)] == 7:
        win = compare(four_of_a_kind_kicker(player), four_of_a_kind_kicker(computer))
    elif ranks[what_is_my_hand(player)] == 8:
        if straight_flush_kicker(player) > straight_flush_kicker(computer):
            win = "player"
        elif straight_flush_kicker(player) < straight_flush_kicker(computer):
            win = "computer"
        else:
            win = "no one"
    elif ranks[what_is_my_hand(player)] == 9:
        pass
    return win


# main
os.system('mode con: cols=100 lines=40')
player_money = 100000
computer_money = 100000
entrance_fee = 1000
ranks = {'High Card': 0, 'One Pair': 1, 'Two Pair': 2, 'Three of a Kind': 3, 'Straight': 4, 'Flush': 5, 'Full House': 6,
         'Four of a Kind': 7, 'Straight Flush': 8, 'Royal Straight Flush': 9}
card_num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_type = ['♠', '♥', '♣', '♦ ']
cards = [PokerCard(i, j) for i in card_type for j in card_num]
empty_card = PokerCard('  ', '*')
computer_hand_show = [empty_card, empty_card]
player_name = input('Enter your name : ')
os.system("cls")
print('Welcome to Paul&Jun\'s Texas Hold\'em, %s.' % player_name)
while True:
    while True:
        menu = print_menu()
        if menu == '4':
            break
        elif menu == '3':
            while True:
                poker_hand_ranking()
                explanation = select_explanation()
                if explanation == 0:
                    os.system("cls")
                    break
                else:
                    print_explanation(explanation)
        elif menu == '2':
            how_to_play()
            os.system("cls")
        elif menu == '1':
            break
        else:
            print("Not Valid Menu!")
    if menu == '4':
        os.system("cls")
        break
    while player_money > 0 or computer_money > 0:  # 플레이어 또는 컴퓨터의 돈이 0이 되기 전까지는 계속 반복
        cards_temp = cards.copy()  # cards의 복사본 pop메소드를 쓰기 위해 지정함
        community_cards = [empty_card, empty_card, empty_card, empty_card, empty_card]
        player_hand = []
        computer_hand = []
        reward = 0
        print_screen(computer_hand_show, computer_hand_show, community_cards)
        while True:  # 공개 != 출력, 즉 공개한다고 화면에 출력하는 것은 아니다.
            if game_state(community_cards.count(empty_card)) == "Pre-flop":
                dealing_animation(0.005)
                if will_you_pay_entry():
                    player_money -= entrance_fee
                    computer_money -= entrance_fee
                    reward += 2 * entrance_fee
                else:
                    break
                deal()
                print_screen(player_hand, computer_hand_show, community_cards)
                if will_you_bet():
                    betting()
                    community_cards[0] = cards_temp.pop(cards_temp.index(r.choice(cards_temp)))
                    print_screen(player_hand, computer_hand_show, community_cards)
                    time.sleep(1)
                else:
                    computer_money += reward
                    break
            elif game_state(community_cards.count(empty_card)) == "onGoing":
                community_cards[1] = cards_temp.pop(cards_temp.index(r.choice(cards_temp)))
                print_screen(player_hand, computer_hand_show, community_cards)
                time.sleep(1)
                community_cards[2] = cards_temp.pop(cards_temp.index(r.choice(cards_temp)))
                print_screen(player_hand, computer_hand_show, community_cards)
            elif game_state(community_cards.count(empty_card)) == "Flop":
                if will_you_bet():
                    betting()
                    community_cards[3] = cards_temp.pop(cards_temp.index(r.choice(cards_temp)))
                    print_screen(player_hand, computer_hand_show, community_cards)
                else:
                    computer_money += reward
                    break
            elif game_state(community_cards.count(empty_card)) == "Turn":
                if will_you_bet():
                    betting()
                    community_cards[4] = cards_temp.pop(cards_temp.index(r.choice(cards_temp)))
                    print_screen(player_hand, computer_hand_show, community_cards)
                else:
                    computer_money += reward
                    break
            else:
                if will_you_bet():
                    betting()
                    print_screen(player_hand, computer_hand, community_cards)
                    evaluation_hand_player = player_hand + community_cards
                    evaluation_hand_computer = computer_hand + community_cards
                    print("Your Hand:", what_is_my_hand(evaluation_hand_player))
                    print("Computer Hand:", what_is_my_hand(evaluation_hand_computer))
                    player_status = ranks[what_is_my_hand(evaluation_hand_player)]
                    computer_status = ranks[what_is_my_hand(evaluation_hand_computer)]
                    if player_status > computer_status:
                        print("You win. You will collect the prize.")
                        player_money += reward
                    elif player_status < computer_status:
                        print("You lose. Computer will collect the prize.")
                        computer_money += reward
                    else:
                        winner = tied(evaluation_hand_player, evaluation_hand_computer)
                        if winner == 'player':
                            print("You win! You will collect the prize.")
                            player_money += reward
                        elif winner == 'computer':
                            print("You lose! Computer will collect the prize.")
                            computer_money += reward
                        else:
                            print("TIED!!!")
                            player_money += reward // 2
                            computer_money += reward // 2
                else:
                    computer_money += reward
                input("Press any key to continue.")
                break
    if player_money == 0:
        print('YOU LOSE!! TOO BAD!')
    elif computer_money == 0:
        print('CONGRATS!!! YOU WIN!!!')
print("███████  █     █     █    █     █  █     █")
print("   █     █     █    █ █   █ █   █  █    █")
print("   █     ███████   █   █  █  █  █  █   █")
print("   █     █     █   █████  █   █ █  ██ █")
print("   █     █     █  █     █ █    ██  █    █")
print("   █     █     █  █     █ █     █  █     █")
print("\n\n")
print("       █     █   █████   █     █     ██")
print("        █   █   █     █  █     █     ██")
print("         █ █    █     █  █     █     ██")
print("          █     █     █  █     █     ██")
print("          █     █     █  █     █")
print("          █      █████    █████      ██")
input()
