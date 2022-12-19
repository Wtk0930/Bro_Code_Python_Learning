# tuple = a collection which is ordered and unchangeable used to group together related data

student = ("Bro", 21, "male");

print(student.count(21));
print(student.index("male"));

for x in student:
    print(x);

# check if "Bro" is in the tuple of student
if "Bro" in student:
    print("Bro is here");
