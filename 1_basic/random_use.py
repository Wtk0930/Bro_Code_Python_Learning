import random;

# generate a random number between one and six
x = random.randint(1, 6);
# generate a random number between zero and one
y = random.random();

myList = ["rock", "paper", "scissors"];
# Choose a random element from a non-empty sequence.
z = random.choice(myList);

cards = [1,2,3,4,5,6,7,"J","Q","K","A"];
# shuffle the list
random.shuffle(cards);

print(cards);
