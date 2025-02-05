PeopleAge = {
    "John": 25,
    "Jane": 24,
    "Jack": 27,
    "Jill": 26,
    "James": 28,
    "Jenny": 29
}

def GetAge(name):
    return PeopleAge[name]

print(GetAge("Jane"))