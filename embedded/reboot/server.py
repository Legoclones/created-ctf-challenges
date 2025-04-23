### IMPORTS ###
import os, time, sys


### INPUT ###
hostname = 'bababooey'

while True:
    print('=== MENU ===')
    print('1. Set hostname')
    print('2. Reboot')
    print()
    choice = input('Choice: ')

    if choice == '1':
        hostname = input('Enter new hostname (30 chars max): ')[:30]

    elif choice == '2':
        print("Rebooting...")
        sys.stdout.flush()
        time.sleep(30)
        os.system(f'cat /etc/hosts | grep {hostname} -i')
        print('Reboot complete')

    else:
        print('Invalid choice')