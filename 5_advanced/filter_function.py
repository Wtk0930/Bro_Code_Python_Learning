# filter() = creates a collection of elements from an iterable for which a function returns True
#
# filter(function, iterable)

friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20),
];

# get the people over the drinking age
print(list(filter(lambda item:item[1] >= 18, friends)));
