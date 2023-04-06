f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866

for suburb, population in f_suburbs.items():
    if suburb[:6] != "Forest" and population is not None:
        print(f'{suburb}: {population}')






for i in range(1,101):
    if i % 3 == 0 and i % 5 !=0:
        print(f'{i}: Fizz')
    elif i % 5 == 0 and i% 3 !=0:
        print(f'{i}: Buzz')
    elif i % 3 == 0 and i % 5 ==0:
        print(f'{i}: FIZZ BUZZ')
    else:
        print(i)

l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

for i, x in enumerate(l):
    print(f"{i}: {x}")


first_names = ['Dwayne', 'Ryan', 'Mark', 'Ben', 'Vin']
middle_names = ['"The Rock"', 'Rodney', 'Robert Michael', 'Geza', None]
last_names = ['Johnson', 'Reynolds', 'Wahlberg', 'Affleck', 'Diesel']

for i in last_names:
    for f in first_names:
        for m in middle_names:
            if m is not None:
                print(f'{f} {m} {i}')
            else:
                print(f'{f} {i}')




