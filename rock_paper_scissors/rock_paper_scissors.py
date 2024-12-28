import random

print("\t\t\t\t##############################\n\n\t\t\t\t*******START THE GAMING*******\t\n\n\t\t\t\t##############################")

choices = ['r','p','s']

again = True

while (again):
    user_input = input("Enter Your Move: (r for rock) , (p for paper) , (s for scissors)\n")
    pc_input = random.choice(choices)

    if user_input not in choices:
        print("\t\t\tInvalid Move!\n\t\t\t#####Try Again#####")
        continue
    print(f"Your Moved: {user_input}\nPC Moved: {pc_input}\n")

    if (user_input == pc_input):
        print("\t\t\tIt's A Tie!\n\t\t\t#####Try Again#####")
        continue

    elif((user_input=='r' and pc_input == 's') or
        (user_input=='s' and pc_input == 'p') or
        (user_input=='p' and pc_input == 'r')):
        print("\t\t\t\tYou Won!")

    else:
        print("\t\t\t\tYou lost!")
    
    answer = input("\t\t\t#####Play Again? (y/n)#####")
    if (answer == 'n'):
        again = False
        
print("\t\t\t\t######################\n\n\t\t*******I hope you enjoyed and don't forget to visit us again*******\t\n\n\t\t\t\t######################")

