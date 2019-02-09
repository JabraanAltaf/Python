#Creating a hangman which gives the user the same number of guessing a correct letter as the character length of a randomly chosen animal name from a animal names list. Once, the number of guesses have run out, the user will be asked to input what they think the random word is.
#Sources used to help: https://repl.it/@sebastiansilva/HangMan-V4
#Extended Requirements:
# 1) Output with correct guesses in relative position
# 2)  User enters the same character twice as a guess

#Input of random function
import random
animals = ["dog","cat","horse","elephant","giraffe","zebra","monkey","cow","mouse","snake","tiger","lion","kangaroo","lizard","spider","gorilla","ape","deer","goat","fish"]
#list for animal names
alreadyList = []
#lists above will be appended by user's letter input

#Function for if the user wants to restart the game
def playagain():
    print ("GAME OVER!")
    print ("--------------------------------------------")

    option =input("Want to play again? (Enter Y: Yes or N: No): ")
    option = option.upper()#Using modularisation to force input of letter to be uppercase.

    if option == "N":
        import sys # Helps close the program - source: https://stackoverflow.com/questions/2823472/is-there-a-method-that-tells-my-program-to-quit
        sys.exit(0)

    if option == "Y":
      startgame()
      
#Function for getting the random word        
def getWord(): 
  secretword = random.choice(animals)
  return secretword

#Main function for the game
def hangman():
  secretword = getWord() #Calls secretword
  letterdisplay= [] #List for displaying letters
  letterdisplay.extend(secretword) #Extends list to include secretword
  correctList = [] # List for correct letters
  lettersList = [] # List for letters used
  wrongList = [] # List for wrong letters
  guess=len(secretword) #Number of guesses is equal to character length of random word

  print ("Random Animal Name has",guess,"letters")

# *Extended Requirement* (displaying user inputs)
#Using iteration for the list to display underscores in place of the letters in the random word
  for i in range(len(letterdisplay)):
      letterdisplay[i] = "_" 
  print (' '.join(letterdisplay)) #puts a space between the underscores
  print ()

#Loop used until guesses run out
  while True:
   letter = input("Guess a letter (only) in the Name: ")
   letter = letter.lower() #modularised to account for lowercase letters of randomword
   
   for i in range(len(letterdisplay)):
       if secretword [i] == letter:
          letterdisplay[i] = letter
  #Using iteration to replace the blank letters with correctly guessed letters

   print (' '.join(letterdisplay)) #prints the correct letters and dashes (if there are any)

# Some conditions used to output whether a letter guessed is used twice/correct/wrong or not a letter
   if letter in lettersList and letter.isalpha():
     print ("Letter already in use!") # *Extended Requirement* (already guessed letters)
   if letter in secretword and letter.isalpha:
		 print ("Correct")
		 guess = guess-1 #reduces guess number by 1
		 print ("Guesses left: ",guess)
		 lettersList.append(letter)
		 print ("Letters so far: ",lettersList)
		 correctList.append(letter)
   elif letter not in secretword and letter.isalpha():
		  print ("Incorrect")
		  guess = guess-1 #reduces guess number by 1
		  print ("Guesses left: ",guess)
		  lettersList.append(letter)
		  print ("Letters so far: ",lettersList)
		  wrongList.append(letter)
#ends game if user inputs a non letter and asks to play again
   else:
		 print ("You have entered a non-letter")
		 print ("Game Over!")
		 print ("RETURNING TO MAIN MENU")
		 print ("----------------------------------")
		 main()

#When all guesses are finished  
   if guess == 0:
		 print ("No Guesses left!")
		 print ("----------------------------------")
		 print ("Letters used: ",lettersList)
		 print ("Correct letters were: ",correctList) #prints correct letters list
		 print ("Wrong letters were: ",wrongList) #prints wrong letters list
		 print ("----------------------------------")
		 finalword = input("Guess the Word: ") #Asks user to make their guess
		 finalword = finalword.lower()
		 
		 if finalword == secretword:
			print ("Correct Answer!!!")
		 else:
			print ("Incorrect Answer!")
			print ("Correct Answer was: ",secretword) #prints correct answer
		 playagain() #Asks whether to restart the program

#Prompts user on whether they want to start the game
def startgame():
        option =input("Do you want to start the game? (Press Y for Yes/N for No): ")
        option =option.upper()
        if option == "N":
			 main() #returns to Main Menu
			 return
        if option == "Y":
			 print ("Game is starting...")
			 print ("\n")
			 hangman() #starts the game

def main(): #defining the Main Menu function
    print ("Main Menu")
    print ("--------------")
    print ("A: Numbers")
    print ("B: Strings")
    print ("C: Games")
    print ("X: Exit")
    print ()
    option =input("Enter An Option (A,B,C, or X): ")
    option = option.upper()#Using modularisation to force input of letter to be uppercase.

    if option == "X":
        import sys # Helps close the program - source: https://stackoverflow.com/questions/2823472/is-there-a-method-that-tells-my-program-to-quit
        sys.exit(0)

    if option == "C":
      startgame() #loads up starting prompt

         
#Start
main()
