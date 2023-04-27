my_words = ['the', 'cat', 'in', 'the', 'hat']

# print each word and its length
for w in my_words: 
    print(w, len(w))
print("----====----")

# modify a collection by copying to new collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del[users[user]]

for user, status in users.items():
    print(user, ', ', status)

print("----====----")

# modify a collection by creating a new collection
users = {'Hans': 'active', 'Éléonore': 'active', '景太郎': 'inactive'}
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for user, status in active_users.items():
    print(user, ', ', status)

print("----====----")

# print 0 - 19
for i in range(3):
    print(i)
print("----====----")
