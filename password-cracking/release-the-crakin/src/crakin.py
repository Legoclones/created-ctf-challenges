import random

# initializations
questions = [
    {"question": "\"A hash is a mathematical function that converts an input of arbitrary length into an encrypted output of a _____ length.\"", "answer": "fixed"},
    {"question": "Hashing algorithms used by Windows nowadays", "answer": "ntlm"},
    {"question": "Hashing algorithm identified by $1$", "answer": "md5"},
    {"question": "OSX only stores passwords as hashes on a per-user basis. If the user is Paulina, where is her password hash stored? (note - case sensitive)", "answer": "/var/db/dslocal/nodes/Default/users/Paulina.plist"},
    {"question": "What is the SHA3 224 hash of 1234567890?", "answer": "9877af03f5e1919851d0ef4ce6b23f1e85a40b446d93713f4c6e6dcd"},
    {"question": "What is the password that creates the hash 7ce21f17c0aee7fb9ceba532d0546ad6?", "answer": "1234"},
    {"question": "The hash is 760ebb335f78b8f80f7ec0dfb89f2aab, the password is a five-letter name followed by a year. What is the password?", "answer": "chris2003"},
    {"question": "Not a correct horse, battery, or staple, hash is 24d9c99595080b241b3b4eb0cba8d8f4. Password? (case sensitive)", "answer": "Tr0ub4dor&3"},
    
    {"question": "What password gives you the hash 31d6cfe0d16ae931b73c59d7e0c089c0?", "answer": ""},
    {"question": "Number of bits in an MD5 hash", "answer": "128"},
    {"question": "The hash is $2a$10$NtsNKjwL1OJyAfBZqsk4cens77MyIAuqYD83r4/X182NjOJ1u2l5q, password? (case sensitive)", "answer": "1qazZAQ!"},
    {"question": "Name of randomly-generated characters added to a password before hashing to prevent the usage of rainbow tables", "answer": "salt"},
    {"question": "Hashcat hash mode 24600 is called...", "answer": "sqlcipher"},
    {"question": "Hashcat attack mode 9 is called...", "answer": "association"},
    {"question": "John the Ripper was developed by...", "answer": "openwall"},
    {"question": "The password for the hash 9c877decdc3ae6e607c92a29d9e6356f6c5fa0b8b963ef6b195bc96354cfec88f671597677f602c7b725f77261b57e66c278a5a96597121f0468900b8c2db494 is?", "answer": "1242"},
]
random.shuffle(questions) # randomize order of questions
HASH = "327a6c4304ad5938eaf0efb6cc3e53dc" # flag


# intro
print("Each question you answer correctly will give you another letter of the hash.")
print("Once you have answered all the questions correctly, you will be able to crack the hash and get the password.")
print("All answers should be lowercase unless specified otherwise.")
print("The flag is in the format byuctf{password}")
print("Good luck!")


# loop through questions
for question in questions:
    print("\nQuestion: " + question["question"])
    answer = input("Your answer: ")

    if answer == question["answer"]:
        print("Correct!")
        print(HASH[:(questions.index(question)+1)*2])

    else:
        print("Wrong! Now you have to start ALL OVER!")
        quit()


print("\nYou answered all the questions correctly! You can now crack the hash and get the password.")
