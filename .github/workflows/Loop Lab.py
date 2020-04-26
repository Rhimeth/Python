for eachPass in range(4):
    print("*")



print(" ")


for eachPass in range(4):
    print("*", end = " ")



print(" ")


for eachPass in range(5):
    for eachPass in range(5):
        print("*", end = " ")

    print("\n")
print("\n")
print("\n")


for v1 in range(6, 1, -1):
    for v2 in range(v1-1):
        print("*", end = " ")

    print("\n")
    
print("\n")
print("\n")


for v1 in range(5):
    for v2 in range(v1 + 1):
        print("*", end = " ")

    print("\n")
    
print("\n") 
print("\n")



for letter in range(5):
    print(chr(65+letter), " ")
print("\n")

stem = ">"
for letter in range(5):
    if letter == 0:
        stem = "-" + stem
    else:
        stem = "--" + stem
    print(stem + chr(65+letter), end = "\n")
print("\n")


stem = "-"
add = 4
addcount = 0
stemsadded = add * addcount
for letter in range(5):
    if letter%2 == 0:
        stem = stem + "-"*(add*addcount)
        print(stem + ">" + chr(65+letter), end = "\n")
        addcount += 1

    else:
        
        print(chr(65+letter), end = "\n")

stem = "_"
add = 3
addcount = 0
stick = "|"
for letter in range(5):
    if letter == 0:
        stem = "_" + stem
    else:
        stem = "___" + stem
    print(stem + chr(65+letter), end = "\n")
    print("      " + stick)
