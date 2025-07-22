

print ("Welcome to my Computer quiz ! ")
print("This quiz will contain 10 questions !")
Playing = input("Do you want to play this game?  :  ")
score = 0

if Playing.lower() == "yes":
    print("OK lets Play and Score your knowledge (^_^)")
else:
    quit()

answer = input("1. What does CPU stands for ? : ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : Central Processing Unit")

answer = input("2. Find the odd term out.\nA) Scanner \t B) Pointing device \t C) OMR \t D)Printer\nAnswer : ")
if answer.lower() == "printer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : D)Printer")

answer = input("3. Which of the following is not a Window 7 Aero feature :\nA)Snap \t B)Peek \t C)Bump \t D)Shake \nAnswer : ")
if answer.lower() == "bump":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : C)Bump")

answer = input("4. Multimedia is used for many purposeslike :\nA)Education \t B)Advertising \t C)Playing Games \t D)All of these \nAnswer : ")
if answer.lower() == "playing games":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : C)Playing Games")

answer = input("5. MS word is a ____ software :\nA)Presentation \t B)Spreadsheet \t C)Word Processing \t D)Mathematical \nAnswer :  ")
if answer.lower() == "word processing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : C)Word Processing")

answer = input("6. Tables group is present in ___ tab :\nA)Insert \t B)Symbol \t C)File \t D)Layout \nAnswer :  ")
if answer.lower() == "insert":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : A)Insert")

answer = input("7. _____ defence department formed ARPA :\nA)India's \t B)Canada's \t C)UK's \t D)USA's \nAnswer :  ")
if answer.lower() == "usa's":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : D)USA's")

answer = input("8. An algorithm can solve ____ problems :\nA)Alphabetical \t B)Mathematical \t C)Both \t D)None of above \nAnswer :  ")
if answer.lower() == "mathematical":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : B)Mathematical")

answer = input("9. The Extentin of MS excel file is  :\nA).xlx \t B).docx \t C).xlxs \t D).xlsx \nAnswer :  ")
if answer.lower() == ".xlsx":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : D).xlsx")

answer = input("10. What does GPU stands for : ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    print("Correct answer is : Graphics Processing Unit")


print("You got  " + str(score) + "  correct question")
print("You got  " + str(score*10) + "%")




