print("Welcome to my computer quiz!")

play = input("Do you wanna play my game? ").lower()

if play != "yes":
    quit()

print("Okay, lets play :)")

score = 0


#first question

ans = input("What does CPU stand for? ").lower()
if ans != "central processing unit":
    print("Incorrect :(")
else:
    print("Correct!")
    score += 1

#second question
ans = input("What does GPU mean? ").lower()
if ans != "graphics processing unit":
    print("Incorrect :(")
else:
    print("Correct!")
    score += 1

#third question
ans = input("What does LCD mean? ").lower()
if ans != "liquid crystal display":
    print("Incorrect :(")
else:
    print("Correct!")
    score += 1

print("you got: " + str(score) + " questions correct! :)")