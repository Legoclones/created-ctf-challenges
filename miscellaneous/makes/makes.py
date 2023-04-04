import random

makes = []
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"

# add randomly-generated name
for letter in alphabet:
    for _ in range(12):
        makes.append({ "name": letter+("%08x"%random.getrandbits(32)) })


# add echo 1 or echo l
for make in makes:
    if random.randint(0,1) == 0:
        make["line1"] = "echo"+(random.randint(1,24)*" ")+"1"
    else:
        make["line1"] = "echo"+(random.randint(1,24)*" ")+"l"


# randomly link to another one
random_numbers = [x for x in range(len(makes))]
for make in makes:
    if random.randint(0,11) == 0:
        make["line2"] = "make"
    else:
        randInt = random.randint(0,len(random_numbers)-1)
        make["line2"] = "make "+makes[random_numbers[randInt]]["name"]
        random_numbers.remove(random_numbers[randInt])


# randomize list order
random.shuffle(makes)


# print out
for make in makes:
    print(make["name"]+":\n\t"+make["line1"]+"\n\t"+make["line2"]+"\n")