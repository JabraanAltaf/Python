#Creating a program to roll a 6-sided dice four times and then printing a message based on the outcome of the scores 
def diceRoll(): #Defining function of the Dice Roll
        Option = input("Enter S To Start The Game/ X To Return To Main Menu: ")
        Option = Option.upper() #Using modularisation to force input of letter to be recognised as an uppercase letter
        if Option == "X":
                print ("---------------------------")
                print ("RETURNING TO MAIN MENU")
                print ("---------------------------")
                main () #Returns to Main Menu if "X" is input
        while Option == "S": #Using while loop for when S is input for the Dice Roll game to start
                import random #Enables us to use random function
                dice1= random.randint(1,6) #Using the random integer function to assign a random number between the range of 1 and 6 inclusive to each dice 
                print ("Score For Dice 1 = ",dice1)
                dice2 = random.randint(1,6)
                print ("Score For Dice 2 = ",dice2)
                dice3 = random.randint(1,6)
                print ("Score For Dice 3 = ",dice3)
                dice4 = random.randint(1,6)
                print ("Score For Dice 4 = ",dice4)
                diceScores = (dice1,dice2,dice3,dice4) 
                print ("Four Dices Have Score: ",diceScores) #Prints the scores of all four dices on one line
                if (dice1==dice2==dice3==dice4): #When each dice holds the same value
                        print ("All The Same")
                elif (dice1==dice2==dice3) or (dice1==dice2==dice4) or (dice2==dice3==dice4): #When there are three scores which hold the same value
                        print ("Three The Same")
                elif (dice1==dice2) and (dice3==dice4) or (dice1==dice3) and (dice2==dice4) or (dice1==dice4) and (dice2==dice3): #When there are two pairs of scores
                        print ("Two Pairs")
                elif (dice1==dice2) or (dice2==dice3) or (dice3==dice1) or (dice1==dice4) or (dice2==dice4) or (dice3==dice4): #When two scores hold the same value
                        print ("A Pair")

            # Printing an output message, when there is a run of four dice scores in a straight sequence or a mixed sequence
                elif (dice1 + 1) in diceScores and (dice1 + 2) in diceScores and (dice1 + 3) in diceScores: 
                    print("Run Of Four") 
                elif (dice2 + 1) in diceScores and (dice2 + 2) in diceScores and (dice2 + 3) in diceScores:
                    print("Run Of Four")
                elif (dice3 + 1) in diceScores and (dice3 + 2) in diceScores and (dice3 + 3) in diceScores:
                    print("Run Of Four")
                elif (dice4 + 1) in diceScores and (dice4 + 2) in diceScores and (dice4 + 3) in diceScores:
                    print("Run Of Four")

    
            # Printing an output message, when there is a run of three dice scores in a straight sequence or a mixed sequence
                elif (dice1 + 1) in diceScores and (dice1 + 2) in diceScores:
                    print("Run Of Three")
                elif (dice2 + 1) in diceScores and (dice2 + 2) in diceScores:
                    print("Run Of Three")
                elif (dice3 + 1) in diceScores and (dice3 + 2) in diceScores:
                    print("Run Of Three")
                elif (dice4 + 1) in diceScores and (dice4 + 2) in diceScores:
                    print("Run Of Three")
                
             # Printing an output message, when there is a run of three dice scores in a straight sequence or a mixed sequence and a pair of dice scores.
                elif (dice1 == dice2) or (dice1 == dice3) or (dice1 == dice4) or (dice2 == dice3) or (dice2 == dice4) or (dice3 == dice4):
                    if (dice1 + 1) in diceScores and (dice1 + 2) in diceScores:
                        print("Run Of Three With A Pair")
                    elif (dice2 + 1) in diceScores and (dice2 + 2) in diceScores:
                        print("Run Of Three With A Pair")
                    elif (dice3 + 1) in diceScores and (dice3 + 2) in diceScores:
                        print("Run Of Three With A Pair")
                    elif (dice4 + 1) in diceScores and (dice4 + 2) in diceScores:
                        print("Run Of Three With A Pair")

                else: #Use else function to output a message when each dice score is different and not in a run.
                        print ("Different")
                print ("---------------------------")
                print ("RETURNING TO MAIN MENU")
                print ("---------------------------")
                main() #This returns to the main menu after one game has been played
                break #This breaks the loop
                

def main(): # Defining the Main Menu function
    print ("Main Menu")
    print ("--------------")
    print ("A: Numbers")
    print ("B: Strings")
    print ("C: Games")
    print ("X: Exit")
    print ()
    option =input("Enter An Option (A,B,C, or X): ")
    option = option.upper() #Using modularisation to force input of letter to be uppercase.
    if option == "C":
        diceRoll() #This loads up the dice roll function once the letter "C" is entered
    if option == "X":
        import sys # Helps close the program - source: https://stackoverflow.com/questions/2823472/is-there-a-method-that-tells-my-program-to-quit
        sys.exit(0) #Function terminates the program when "X" is input

#Start
main()
