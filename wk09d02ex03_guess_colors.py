def countCorrect(rainbowColors, userGuesses):
    correctCount = 0
    for i in range(0, 6 + 1, 1):
        if rainbowColors[i] == userGuesses[i]:
            correctCount = correctCount + 1
    
    return correctCount

def getGrade(correctCount):
    if correctCount <= 2:
        grade = "poor"
    else:
        if correctCount <= 5:
            grade = "average"
        else:
            grade = "excellent"
    
    return grade

def getGuesses(userGuesses):
    print("INSTRUCTIONS: Write your answers in SMALL CAPS, NO CAPITAL LETTERS.")
    i = 0
    for i in range(0, 6 + 1, 1):
        print("Enter color #" + str(i + 1) + " of the rainbow:")
        color = input()
        userGuesses[i] = color

def getUserName():
    print("Enter username")
    userName = input()
    
    return userName

# Main
rainbowColors = [""] * (7)

rainbowColors[0] = "red"
rainbowColors[0] = "red"
rainbowColors[1] = "orange"
rainbowColors[2] = "yellow"
rainbowColors[3] = "green"
rainbowColors[4] = "blue"
rainbowColors[5] = "indigo"
rainbowColors[6] = "violet"
userGuesses = [""] * (7)

userName = getUserName()
getGuesses(userGuesses)
correctCount = countCorrect(rainbowColors, userGuesses)
getGrade(correctCount)
grade = getGrade(correctCount)
print("Hello, " + userName)
print("You got " + str(correctCount) + " out of 7 correct.")
print("Your grade: " + grade)
