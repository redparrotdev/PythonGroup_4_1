names = [
    "Victoria",
    "Wade",
    "Chanelle",
    "Victoria",
    "Evan",
    "Tyrone"
    "Neve",
    "Peggy",
    "Tyrone",
    "Peggy",
]
s = set(names)
names = [n for n in s if len(n) >= 5]
print(names)
