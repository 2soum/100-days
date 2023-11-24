import random
def blackjack_advice(user_score, dealer_card):
    if user_score <= 11:
        return "Advice: Hit (Your total is 11 or less.)"
    elif user_score >= 17:
        return "Advice: Stand (Your total is 17 or higher.)"
    elif 12 <= user_score <= 16:
        if dealer_card >= 7:
            return "Advice: Hit (Dealer's card is high.)"
        else:
            return "Advice: Stand (Dealer's card is low.)"
    return "No advice available."

def print_logo():
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    print(logo)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Both went over. It's a draw 😐"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def get_bet(budget):
    while True:
        try:
            bet = int(input("Combien voulez-vous miser ? $"))
            if bet > 0 and bet <= budget:
                return bet
            else:
                print("Mise invalide. Vous devez miser un montant entre 1 et votre budget.")
        except ValueError:
            print("Veuillez entrer un nombre.")


def play_game():
    print_logo()
    budget = 1000  # Budget initial du joueur.

    while budget > 0:
        user_cards = []
        computer_cards = []
        is_game_over = False

        print(f"Budget actuel: ${budget}")
        bet = get_bet(budget)

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            dealer_card = computer_cards[0]

            print(f"Vos cartes: {user_cards}, score actuel: {user_score}")
            print(f"Première carte du croupier: {dealer_card}")
            print(blackjack_advice(user_score, dealer_card))

            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Tapez 'y' pour une autre carte, 'n' pour passer: ")
                if user_should_deal == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"Votre main finale: {user_cards}, score final: {user_score}")
        print(f"Main finale du croupier: {computer_cards}, score final: {computer_score}")
        result = compare(user_score, computer_score)
        print(result)

        if "win" in result:
            budget += bet
        elif "lose" in result:
            budget -= bet
        else:
            # En cas de match nul, le joueur ne gagne ni ne perd.
            pass

        if budget <= 0:
            print("Vous avez épuisé votre budget ! Fin du jeu.")
            break
        else:
            play_again = input("Voulez-vous jouer une autre manche ? (y/n): ")
            if play_again.lower() != "y":
                break

    print("Merci d'avoir joué !")


play_game()
