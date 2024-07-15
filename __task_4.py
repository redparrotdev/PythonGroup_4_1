setNeed = ("молоко", "ХлеБ", "КолбаСА", "ЯЙцА")
print("Need:", ", ".join(i for i in setNeed))

setStore = ("ХЛЕБ", "яйца", "колбаСа")
print("Store:", ", ".join(i for i in setStore))

setStore = set(i.lower() for i in setStore)

d = {i.capitalize(): "Yes" if i.lower() in setStore else "No" for i in setNeed}

for k, v in d.items():
    print(f"<{k}> on the store: [{v}]")

