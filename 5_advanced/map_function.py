# map() = applies a function to each item in an iterable (list, tuple, etc)
#
# map(function, iterable)

store = [
    ("shirt", 20.00),
    ("pants", 25.00),
    ("jacket", 50.00),
    ("socks", 10.00),
];

# 0.14 dollar = 1 yuan
to_yuans = lambda data: (data[0], round(data[1] / 0.14) );
to_dollars = lambda data: (data[0], round(data[1] * 0.14 ));

print(list(map(to_yuans, store)));
