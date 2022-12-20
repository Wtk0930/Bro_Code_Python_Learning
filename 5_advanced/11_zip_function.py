# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc. )
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ['Dude', 'Bro', 'Mister'];
passwords = ('password', 'abc123', 'guest');
login_date = {1: 'wtk', 2: 'lfl', 3:'lfy'};

users = dict(zip(usernames, passwords));
users_2 = zip(usernames, passwords, login_date);

for key, value in users.items():
    print('{}: {}'.format(key, value));

for item in users_2:
    print(item);
