users = [
    {"username": "bob", "password": "supersecure"},
    {"username": "alice", "password": "notsupersecure"},
    {"username": "admin", "password": "byuctf{th1s_1s_th3_cous1n_of_sql1}"},
]

print("Welcome to the Super Secret Roblox Server!")
username = input("Username: ")
password = input("Password: ")

passwordCorrect = False

for user in users:
    exec('if (username == user["username"]) and ("'+password+'" == user["password"]): passwordCorrect = True')

if not passwordCorrect:
    print("Username or password is incorrect")
else:
    print("Correct!")