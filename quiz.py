print("Well come to the quiz!")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Lets play :)")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score))