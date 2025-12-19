users = ['A','B','C','D','E']

print(users)
print(users[1:4])

# Adding items to a list

users.append('F')
print(users)
users.remove('F')
print(users)

# Modifying a value

users[0] = 'a'
print(users)

# Adding at specific position

users.insert(1, 'b')
print(users)

# Deleting a particular index

del users[2]
print(users)

users[0:2] = ['A', 'B']

# List sorting

users.sort(reverse = True)
print(users)

users[0:2] = ['A', 'B']
print(users)

#Pop - removes last value - it can also be stored in a 
# variable for future use






















