

# declare customers name
name = input("Welcome to GC Mini golf! What is your name? ")
numOfPutts = 0
totalScore = 0
par = 3

print(f"Hi, {name}!", end=" ")

# input for how many holes the user will play
while True:
    numOfHoles = int(input("Would you like to play 3 or 6 holes today? "))

# loop for the number of holes played and what they putted

    if numOfHoles == 3 or numOfHoles == 6:
        for x in range(numOfHoles):

            numOfPutts = int(input(f"How many putts for hole {x+1}? (par is 3) "))
            totalScore += numOfPutts - par
        break
    else:
        print("That is not a valid entry. Please choose either 3 or 6 holes.")

print(f"Good game, {name}! Your total score was: {totalScore:+}")
