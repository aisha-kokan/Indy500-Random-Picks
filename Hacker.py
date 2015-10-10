
print("Made by:")
print("Young coders")
name = input("Enter your name:")
print("Welcome to Indy 500 Random Picks,", name)
print("Show Indy500 logo")
print("\n")
print("RULES")
print("1.) The Indy500 Random Pick application is a “Responsive Design” application built for")
print("both Desktops & Mobile Devices.")
print("\n")
print("2.) Indy500 RandomPick application keeps tail-gating audience engaged throughout the")
print("Race by providing real time points updates.")
print("\n")
print("3.) Groups come together and each player is randomly assigned a race-car and is assigned")
print("a random wager.")
print("\n")
print("   5 points deducted for each position a car slips) per lap; ")
print("   5 points added each position a car gains per lap or maintains position")
print("\n")
print("        Laps = 200")
print("\n")
print("        Max score possible =     (100 + (32  *  5))   =  260 points")
print("\n")
print("        Min score possible =	  (100 -  (32  *  5))   = -160 points")
username = input("Enter your username:")
password = input("Enter your password:")
print("Thank you for entering your data")
group = input("Please enter your group name:")
print("Welcome,", username, ", you have been added to the group named", group,".")
answer = input("Is there anyone else you would like to add to your group? (Enter Yes or No)")
if answer == "No" or " No" :
    print("I'm sorry, but you have to have atleast 2 players.")
    answer = input("Is there anyone else you would like to add to your group? (Enter Yes or No)")
    user2 = input("Enter they're username:")
    input("Enter they're password:")
    print(user2, "Has been added to the group named", group)
    print("OK, you may start your 'fantasy Indy500' experience now. Good luck!")
elif answer == " Yes" or "Yes" : 
    user2 = input("Enter they're username:")
    input("Enter they're password:")
    print(user2, "Has been added to the group named", group)
    print("OK, you may start your 'fantasy Indy500' experience now. Good luck!")






