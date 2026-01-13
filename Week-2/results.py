# Lists                 /.append()  /.remove()  /.extend()

results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# .append add list as a sub-list 
results.append(["Bowser", "Donkey Kong Jr."])
print(results)

# remove sub-list
results.remove(["Bowser", "Donkey Kong Jr."])
print(results)

# extend "results" list
results.extend(["Bowser", "Donkey Kong Jr."])
print(results)