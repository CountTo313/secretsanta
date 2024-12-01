import random
from copy import deepcopy


family = {  # name of family member, list of anyone that should be excluded from the family member
    'Lucky Watcher': ['Arrogant Contender'],
    'Arrogant Contender': ['Lucky Watcher'],
    'Tuff Genius': ['Insane Madman'],
    'Insane Madman': ['Tuff Genius'],
    'Irate Watcher': [],
    'Respected Watcher': [],
    'X-pert Samurai': []
}

secretSanta = dict()
names = list(family.keys())
shuffled = deepcopy(names)

for _ in range(1000):
    random.shuffle(shuffled)
    # Traverse givers & receivers with `itertools.pairwise`.
    for giver, receiver in zip(names, shuffled):
        if receiver in family[giver] or receiver == giver:
            secretSanta = dict()
            break
        else:
            secretSanta[giver] = receiver
    else:
        break

if secretSanta:
    sorted_secretSanta = dict(sorted(secretSanta.items()))
    print(f'{"Giver":30}{"Reciever"}')
    print('------------------------------------------------')

    for key, value in sorted_secretSanta.items():
        print(f'{key:30}{value}')
else:
    print('Program failed. ')