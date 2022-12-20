# list comprehension = a way to create a new list with less syntax
#                       can mimic lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if /else  for item in iterable]




# case 1
squares = [];
for i in range(1, 11):
    squares.append(i * i);
print(squares);

# do the same thing as the code above
squares = list(i * i for i in range(1, 11));
# or
#                       list = [expression for item in iterable]
# squares = [i * i for i in range(1, 11)];

print(squares);







# case 2
students = [1,2,3,4,5,6,7,8,9];
passed_students = list(filter(lambda item: item >= 6, students));


# do the same thing as the code above

#                       list = [expression for item in iterable if conditional]
passed_students = [ i for i in students if i >= 6 ];
#                       list = [expression if /else  for item in iterable]
passed_students = [ i if i >= 6 else "Failed" for i in students ];
print(passed_students);
