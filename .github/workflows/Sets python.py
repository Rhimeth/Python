programming = {"Xavier", "Dubem"}
engineering = {"Dera", "Caleb"}

engineering.add("Rayshawn")

#print(programming)
#print(engineering)

programming.add("Rayshawn")

print(programming)
print(engineering)

programming_but_not_engineering = programming.difference(engineering)

print(programming_but_not_engineering)

not_in_both = programming.symmetric_difference(engineering)

print(not_in_both)

programming_and_engineering = programming.intersection(engineering)

print(programming_and_engineering)

all = programming.union(engineering)

print(all)
