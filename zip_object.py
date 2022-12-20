players = ['Nina', 'Bob', 'Alice']

scores = [100, 5, 97]

zip_obj = zip(players, scores)

print(zip_obj)

for name, score in zip_obj:
    print(f"{name}: {score}")