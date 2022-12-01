print("Welcome to my computer quiz!")

play = input("Do you wanna play my game? ")

if play != "yes":
    quit()
else:
    print("Okay, lets play :)")

#first question

ans = input("What does CPU stand for? ").lower()
if ans != "central processing unit":
    print("Incorrect :(")
else:
    print("Correct!")