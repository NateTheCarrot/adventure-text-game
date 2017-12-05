import time

person = input("Hello there! What is your name?:\n")

print("Well, howdy there, {}!".format(person))

time.sleep(2.5)
print("You've been chosen to go on a special adventure. But first, tell me.\n Which class desribes you? (This is really important.)")
time.sleep(5)

print("Type in...\n\n! for warrior, you will be gifted with immense melee strength. Though, you cannot go long range...\n\n* for mage, you have been gifted with mana, a magic essence with great power. However, your mana is limited but can regenerate...\n\n+ for spy, you're skilled at being unnoticed and clever. But when caught, you may be in lots of trouble...\n\n& for pacifist, you work well with leading groups, and are skilled with making allies. However, you must be prepared for a fight...")

heart = input("\n")

if heart == "!":
    print("You have chosen warrior.")
    time.sleep(5)
    start_over = 1
    lol = input("You've woken up with greenery everywhere you see. It is night. \nWill you...\n1. Look around.\n2. Find materials to make a fire. 3. Give it all up (pls no).\n4. Get sleep. Enter the number to choose (this goes fot responses too)")
    if lol == "4"
    print("You decided to go to sleep. It turns cold... You die from hypothermia.")
    huh = input("Do you wish to try again with the same class? Yes or No.")
    if huh == "Yes" or "yes"
    start_over -=1

else:
    print("That isn't a class. Relaunch the program and try again.")


