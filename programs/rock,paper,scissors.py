import random;

choices = ("rock", "paper", "scissors");
lostMap = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock",
}


while True:
    player = None;
    computer = random.choice(choices);

    while player not in choices:
        if player != None:
            print('You choice must be rock, paper or scissors!');
        player = input("rock, paper, or scissors? ").lower();

    print("computer: ", computer);
    print("You: ", player);

    if player == computer:
        print("Tie!");
    elif player == lostMap[computer]:
        print("You win!");
    else:
        print("You lose");

    play_again = None;
    while play_again not in ["yes", "no"]:
        play_again = input("Play again?(yes / no) ").lower();

    if play_again == "no":
        break;
