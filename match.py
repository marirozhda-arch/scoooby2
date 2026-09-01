from pet import Pet
from console_helper import *
import random
import math

energy = 0
patience = 0
socialization = 0
character_ueser = []

print("")
print("")
print("")
print("")
print("") 

answer = input_int()

if answer == 1:
    energy += 1
elif answer == 2:
    energy += 5
else:
    energy += 10

print("")
print("")
print("")
print("")
print("") 

answer = input_int()

if answer == 1:
    patience += 1
elif answer == 2:
    patience += 5
else:
    patience += 10


print("")
print("")
print("")
print("")
print("")

answer = input_int()

if answer == 1:
    socialization += 1
elif answer == 2:
    socialization += 6
else:
    socialization += 10

print("")
print("")
print("")
print("")
print("")

answer = input_int()

if answer == 1:
    energy += 0
    socialization += 0
elif answer == 2:
    energy += 8
    socialization += 10
else:
    energy += 8
    socialization += 2


print("")
print("")
print("")
print("")
print("")

answer = input_int()

if answer == 1:
    patience += 0
elif answer == 2:
    patience += 10
    socialization += 8
else:
    patience += 8
    energy += 5

energy = max(0, min(10, energy))
socialization = max(0, min(10, socialization))
patience = max(0, min(10, patience))

character_ueser.append(energy)
character_ueser.append(patience)
character_ueser.append(socialization)


def find_best_match(pets: list[Pet], character_ueser: list[int]) -> Optional[Pet]:
    if not pets:
        return None

    best_distance = float('inf')
    best_pets = []

    for pet in pets:
        diff = [character_ueser[i] - pet.character[i] for i in range(3)]
        distance = math.sqrt(sum(d**2 for d in diff))

        if distance < best_distance:
            best_distance = distance
            best_pets = [pet]
        elif distance == best_distance:
            best_pets.append(pet)

    return random.choice(best_pets)


