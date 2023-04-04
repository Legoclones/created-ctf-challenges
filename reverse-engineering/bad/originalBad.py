# ctf{i_l0ve_unic0d3_bc_y0u_can_d0_th3_stupid3st_stuff}

answer_key = [16, 33, 19, 40, 22, 12, 25, -35, 35, 18, 12, 34, 27, 22, 16, -35, 17, -32, 12, 15, 16, 12, 38, -35, 34, 12, 16, 14, 27, 12, 17, -35, 12, 33, 21, -32, 12, 32, 33, 34, 29, 22, 17, -32, 32, 33, 12, 32, 33, 34, 19, 19, 42]

answer = input("Flag> ")

if len(answer) != 53:
    print("Incorrect")
    quit()

for x in range(len(answer)):
    if answer_key[x] != ord(answer[x])-83:
        print("Incorrect")
        quit()

print("Success!")