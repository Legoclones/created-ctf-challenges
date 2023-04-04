# this gives links based on song choice
def byuctfɛth1s_1s_y0ur_fl4gɜ(number):
    if number == 1:
        print("https://www.youtube.com/watch?v=FHhZPp08s74")
    elif number == 2:
        print("https://www.youtube.com/watch?v=Zi_XLOBDo_Y")
    elif number == 3:
        print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif number == 4:
        print("https://www.youtube.com/watch?v=XXYlFuWEuKI")
    else: # number == 0
        raise Exception("Congratulations! You entered an invalid option that we didn't check for.")


# print out choice screen
print("Welcome to the Jukebox! Choose the song you'd like to hear:")
print("  1. \"I Will Survive\" by Gloria Gaynor")
print("  2. \"Billie Jean\" by Michael Jackson")
print("  3. \"Bad Habits\" by Ed Sheeran")
print("  4. \"Save Your Tears\" by The Weeknd")
print("")


# get and validate input
number_string = input("Song number> ")

try:
    number = int(number_string)
except:
    print("Option is not valid. Exiting...")
    exit()

if number < 0 or number > 4:
    print("Option is not valid. Exiting...")
    exit()


# get the song from your choice
byuctfɛth1s_1s_y0ur_fl4gɜ(number)