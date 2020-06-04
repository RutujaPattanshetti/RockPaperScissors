
import random

COMMENT_PLAYER= "Player wins!"
COMMENT_COMPUTER= "Computer wins!"
COMMENT_TIED= "Tied!"
count_computer = 0
count_player = 0


def main():
    print ("Welcome to the Rock, Paper, Scissors Game!\n(Best of 3)")
    print ()


    while True:
        user_input= input("Take your turn! Rock, Paper or Scissors? \n")
        if user_input=="":
            print("Please try again with a valid input")
            input ("Take your turn! Rock, Paper or Scissors? \n")

        random_numbers = (random.randint(0, 2))


        if random_numbers== 0:
            new_value= check_value(0, "Rock")
            print("Computer response: Rock")
        if random_numbers== 1:
            new_value= check_value(1, "Scissors")
            print("Computer response: Scissors")
        if random_numbers== 2:
            new_value= check_value(2, "Paper")
            print("Computer response: Paper")


        logic(user_input,new_value)
        end_game(count_computer, count_player)





""" Rock WINS against scissors, rock TIED with rock, rock LOSE against paper
    Paper WINS against rock, paper TIED with paper, paper LOSE against Scissors
    Scissors WINS against paper, Scissors TIED with scissors, Scissors LOSE against rock"""

def logic (move_1, move_2):

    if (move_1== "Rock" and move_2=="Scissors") or (move_1=="Paper" and move_2== "Rock") or (move_1=="Scissors" and move_2=="Paper"):
        print (COMMENT_PLAYER)
        count_player= count_player+1


    elif move_1==move_2:
        print (COMMENT_TIED)
        count_player= count_player
        count_computer= count_computer
    else:
        print (COMMENT_COMPUTER)
        count_computer= count_computer+1


"""TRIED THIS TO ASSIGN NUMBER WITH STRING"""

def check_value(random_numbers, title):
    random_numbers== title
    return (title)

def end_game(count_1, count_2):
    if count_1==3:
        print("The game has ended. You lost!")

    if count_2==3:
        print("The game has ended. You won!")




if __name__ == '__main__':
    main()
