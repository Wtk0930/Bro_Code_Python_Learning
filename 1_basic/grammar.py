import time
# if

age = int(input("How old are you"));


# and or not
if age >= 18 and age < 100:
    print("You are a adult");
elif age == 100:
    print("You are a century old");
elif age < 0:
    print("You haven't been born yet");
else:
    print("You are a child");

# # while loop
# while 1 == 1:
#     print("stepsister is stuck");

# for loop
# only iterable object can be used in for loop
for i in range(10, 0, -1):
    print(i)
    # second
    time.sleep(1)

for i in "OBJECT":
    print(i);

# nested loop
rows = int(input("how many rows?"));
columns = int(input("how many columns?"));

for i in range(rows):
    for j in range(columns):
        print('*', end="");
    print();


# continue and break pass
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ");
    if name != '':
        break;

phone_number = "123-456-789";

for i in phone_number:
    if i == "-":
        continue;
    print(i);

for i in range(1, 13):
    if i == 5:
        pass
    else:
        print(i);
