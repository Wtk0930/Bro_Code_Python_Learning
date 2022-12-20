# reduce() = apply a function to an iterable and reduce it to a single cumulative value
#           performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)
import functools


# process
# step1:  ["HE", "L", "L", "O"]
# step2:  ["HEL", "L", "O"]
# step3:  ["HELL", "O"]
# step4:  ["HELLO"]



letters = ["H", "E", "L", "L", "O"];
word = functools.reduce(lambda cur, item: cur  + item, letters);
print(word);
