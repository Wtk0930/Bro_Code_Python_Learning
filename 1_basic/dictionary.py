# dictionary = a changeable, unordered collection of unique key:value pairs Fast because they use hashing, allow us to access a value quickly

capital = {
            'China': "ZHEJIANG province",
            "India": "Beijing",
            "Russia": "Mexico"
        };

# update
capital["China"] = "Beijing";
capital.update({"Germany": 'Berlin'});
# remove
capital.pop('China');
# remove all
capital.clear();

print(capital['Russia'], capital.get('Russia'));
print(capital.keys());
print(capital.values());
print(capital.items());

for key, value in capital.items():
    print(key,":",value);
