import time
# epoch = a date and time from which a computer measures system time


# Convert a time in seconds since the Epoch to a string in local time.
# This is equivalent to asctime(localtime(seconds)).
# When the time tuple is not present, current time as returned by localtime() is used.
print(time.ctime(0));
# now
print(time.ctime());


# return current seconds since epoch
print(time.time());

time_object = time.localtime();
print(time_object);
# format time string
localTime = time.strftime('%B %D %Y %H:%M:%S', time_object);
print(localTime);

time_string = '20 April, 2022';
print(time.strptime(time_string, '%d %B, %Y'));


# (year, mouth, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2022, 12,  20, 6, 53, 0, 1, 0, 0)
print(time.asctime(time_tuple));
# convert tuple or object to seconds
print(time.mktime(time_tuple));
