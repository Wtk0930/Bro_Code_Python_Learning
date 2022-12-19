# -------------------------------
def new_game():
    guesses = [];
    correct_guesses = 0;
    question_num = 1;

    for key in questions.keys():
        print(key);
        for item in options[question_num - 1]:
            print(item);
        print('__________________________');

        guess = input("Enter (A, B, C, or D)").upper();
        guesses.append(guess);


        correct_guesses += check_answer(questions.get(key), guess);

        question_num += 1;

    display_score(correct_guesses , guesses);


# -------------------------------
def check_answer(answer: str, guess: str):
    if answer == guess:
        print("Correct!");
        return 0;
    else:
        print("Wrong");
        return 1;



# -------------------------------
def display_score(correct_guesses:int, guesses: list):
    print('------------------');
    print("RESULTS");
    print('------------------');

    print("Answers: ", end='');
    for i in questions:
        print(questions.get(i), end="");
    print();

    print("Guesses: ", end='');
    for i in guesses:
        print(questions.get(i), end="");
    print();

    score = int(correct_guesses / len(questions) * 100);
    print("Your score is: " + str(score) + "%");


# -------------------------------
def play_again():
    response = input("Do you want to play again?").upper();

    if response == "YES":
        return True;
    else:
        return False;


questions = {
    "Who created python?": "A",
    "What year was Python created?": "B",
    "Python is tributed to which comedy group?": "C",
    "Is the earth round?": "A",
};

options = [
                ["A. a", "B. b", "C. c", "D. d"],
                ["A. a", "B. b", "C. c", "D. d"],
                ["A. a", "B. b", "C. c", "D. d"],
                ["A. a", "B. b", "C. c", "D. d"],
        ];

new_game();
while play_again():
    new_game();
