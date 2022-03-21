import random

t=input("It's time for toss choose odd or even: ")
if(((t[0]=='e' or t[0]=='E') and (t[1]=='v' or t[1]=='V') and (t[2]=='e' or t[2]=='E') and (t[3]=='n' or t[3]=='N') and len(t)==4) or ((t[0]=='o' or t[0]=='O') and (t[1]=='d' or t[1]=='D') and (t[2]=='d' or t[2]=='D') and len(t)==3)):
    if (t == 'even'):
        tt = 1
    else:
        tt = 2
    u = float(input("Choose number between 1-6: "))
    u=int(u)
    if (u >= 1 and u <= 6):
        toss = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6]
        random.shuffle(toss)
        print("Computer has choosen ", toss[1])
        if ((u + toss[1]) % 2 == 0):
            print("It's even")
            uu = 1
        else:
            uu = 2
            print("It's odd")
        if (uu == tt):
            print("You've won the toss")
            ze=1
        else:
            print("Computer has won the toss")
            ze=2
        print("\n")
        act = ["bat", "ball"]
        random.shuffle(act)
        if(ze==1):
            c=input("Enter wether you choose to bat or ball: ")
            print("\n")
            if ((c[0]=='b' or c[0]=='B') and (c[1]=='a'or c[1]=='A') and (c[2]=='t'or c[2]=='T') and len(c)==3):
                print("You are going to bat")
                random.shuffle(toss)
                me = 0
                to = 0
                while me != toss[2]:
                    me = int(input("Enter your number: "))
                    if (me <= 6 and me >= 1):
                        random.shuffle(toss)
                        if (me == toss[2]):
                            print("Computer has entered ", toss[2], " you are out!")
                            print("Your total score is ", to)
                            print("\n")
                        else:
                            to = to + me
                            print("Computer has entered ", toss[2], " and your score so far is ", to)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
                print("You are going to ball and you have to defend ", to + 1)
                print("\n")
                m = 0
                m = int(m)
                fs = 0
                while (m != toss[2]):
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " computer is out!")
                            print("computer's total score is ", fs)
                            print("\n")
                            print("You've won the game!!")
                            print("congratulations!!!!!")
                        else:
                            fs = fs + toss[2]
                            if (fs > to):
                                print("Computer has entered ", toss[2], " and computer's score is ", fs)
                                print("\n")
                                print("You've lost the game!!")
                                print("Better luck next time!!!!!")
                                m = toss[2]
                            else:
                                print("Computer has entered ", toss[2], " and computer's score so far is ", fs)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
            elif ((c[0]=='b' or c[0]=='B') and (c[1]=='a'or c[1]=='A') and (c[2]=='l'or c[2]=='L') and (c[3]=='l'or c[3]=='L') and len(c)==4):
                print("You are going to ball")
                random.shuffle(toss)
                m = 0
                to = 0
                while m != toss[2]:
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " computer is out!")
                            print("Computer's total score is ", to)
                        else:
                            to = to + toss[2]
                            print("Computer has entered ", toss[2], "and computer's score so far is ", to)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
                print("\n")
                print("You are going to bat and your target is ", to + 1)
                m = 0
                m = int(m)
                fs = 0
                while (m != toss[2]):
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " you are out!")
                            print("Your total score is ", fs)
                            print("\n")
                            print("You've lost the game!!")
                            print("Better luck next time!!!!!")
                        else:
                            fs = fs + m
                            if (fs > to):
                                print("\n")
                                print("You've won the game!!")
                                print("congratulations!!!!!")
                                m = toss[2]
                            else:
                                print("Computer has entered ", toss[2], " and your score so far is ", fs)
            else:
                print("please enter only either bat or ball!!!")
        else:
            print("Computer has chosen to "+act[0])
            c="iseij"
            if (act[0] == 'ball'):
                print("You are going to bat")
                print("\n")
                random.shuffle(toss)
                m = 0
                m = int(m)
                to = 0
                while m != toss[2]:
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " you are out!")
                            print("Your total score is ", to)
                            print("\n")
                        else:
                            to = to + m
                            print("Computer has entered ", toss[2], " and your score so far is ", to)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
                print("You are going to ball and you have to defend ", to + 1)
                print("\n")
                m = 0
                m = int(m)
                fs = 0
                while (m != toss[2]):
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " computer is out!")
                            print("computer's total score is ", fs)
                            print("\n")
                            print("You've won the game!!")
                            print("congratulations!!!!!")
                        else:
                            fs = fs + toss[2]
                            if (fs > to):
                                print("Computer has entered ", toss[2], " and computer's score is ", fs)
                                print("\n")
                                print("You've lost the game!!")
                                print("Better luck next time!!!!!")
                                m = toss[2]
                            else:
                                print("Computer has entered ", toss[2], " and computer's score so far is ", fs)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
            elif(act[0] == 'bat'):
                print("You are going to ball")
                print("\n")
                random.shuffle(toss)
                m = 0
                m = int(m)
                to = 0
                while m != toss[2]:
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " computer is out!")
                            print("Computer's total score is ", to)
                        else:
                            to = to + toss[2]
                            print("Computer has entered ", toss[2], "and computer's score so far is ", to)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
                print("\n")
                print("You are going to bat and your target is ",to+1)
                print("\n")
                m=0
                m=int(m)
                fs=0
                while (m != toss[2]):
                    m = int(input("Enter your number: "))
                    if (m <= 6 and m >= 1):
                        random.shuffle(toss)
                        if (m == toss[2]):
                            print("Computer has entered ", toss[2], " you are out!")
                            print("Your total score is ", fs)
                            print("\n")
                            print("You've lost the game!!")
                            print("Better luck next time!!!!!")
                        else:
                            fs = fs + m
                            if(fs>to):
                                print("Computer has entered ", toss[2], " and your score is ", fs)
                                print("\n")
                                print("You've won the game!!")
                                print("congratulations!!!!!")
                                m=toss[2]
                            else:
                                print("Computer has entered ", toss[2], " and your score so far is ", fs)
                    else:
                        print("Please enter a number between 1 to 6 only!!!")
    else:
        print("Please choose a number between 1 to 6 only!!!")
else:
    print("Please enter either even or odd only!!!")