import random
def get_choices():
    player_choice = input("Enter your choice :")
    option = ["rock" , "paper" ,"scissor"]
    computer_choice = random.choice(option)
    choice = {"player" : player_choice , "computer" : computer_choice}
    return choice

def check_win(player,computer):
    # print ("you chose " + player , "computer chose " + computer)
    print(f"you chose {player} , computer chose {computer}")
    if player ==computer :
        return "Its a tie!"
    elif player == "rock" and computer == "paper":
        return "computer won"
    elif player == "paper" and computer == "scissor":
        return "computer won"
    elif player == "scissor" and computer == "rock":
        return "computer won"
    else:
        return "player won"

choice = get_choices()
result = check_win(choice ["player"], choice["computer"])
print(result)

# def greeting ():
#     return "Hi"

# response = greeting()
# print (response)