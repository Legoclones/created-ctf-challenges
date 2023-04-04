import pexpect

FLAG = "byuctf{l34rn1ng_t0_us3_n3tc4t_1s_v3ry_1mp0rt4nt}"

# put this in an infinite loop so after someone connects and gets a response, the server spins up again
while True:
    try:
        # spawn connection
        result = pexpect.spawn("nc -lvp 40002")
        result.expect("connect to .*")
    except KeyboardInterrupt:
        print("\nCTRL+C found. Exiting...")
        exit()

    # parse client port number
    try:
        client_port = int(result.after[-7:-2])

        # if port number is correct, print flag
        if client_port == 42069:
            result.sendline(FLAG)
        else:
            result.sendline("Incorrect source port")
    except:
        print("Error in parsing,",result.after[-7:-2],"is not a valid number")

    result.kill(0)