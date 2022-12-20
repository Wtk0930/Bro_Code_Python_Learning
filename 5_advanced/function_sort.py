# sort() method     = used with lists
# sorted() function   = used with iterable



# case 1
students = ["Squidward", "Sandy", "Patrick", "Spongbb", "Mr.Krabs"];

# only for the list
students.sort(reverse=True);

for i in students:
    print(i);


studentss = ("Squidward", "Sandy", "Patrick", "Spongbb", "Mr.Krabs");
# used with iterable
sorted_student = sorted(students,reverse=True);
print(sorted_student)



# case 2
print("-------------------{}------------------".format("case_2"))
studentsss = [
    ("Squidward", "F", 60),
    ("Sandy", "A", 33),
    ("Patrick", "D", 36),
    ("Spongbb", "B", 20),
    ("Mr.Krabs", "C", 78),
];

studentsss.sort(key=lambda grades:grades[1] , reverse=True);

for i in studentsss:
    print(i);
