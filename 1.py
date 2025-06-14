import pickle
d='Hellod world'

with open('data.txt', 'wb') as file:
    pickle.dump(d, file)
with open('data.txt', 'rb') as file:
    print(file)
    print(pickle.load(file))





