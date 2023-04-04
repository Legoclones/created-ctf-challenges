users = [
    {"username": "bob", "password": "supersecure"},
    {"username": "alice", "password": "notsupersecure"},
    {"username": "admin", "password": "haha_this_is_not_the_flag._rce??"},
]

print("Welcome to the Super Secret Roblox Server!")
username = input("Username: ")
password = input("Password: ")

if "open" in password:
    print("Nope")
    exit()

passwordCorrect = False

for user in users:
    try:
        exec('if (username == user["username"]) and ("'+password+'" == user["password"]): passwordCorrect = True')
    except:
        print("Something went wrong. Please try again.")
        exit()

if not passwordCorrect:
    print("Username or password is incorrect")
else:
    print("Correct!")