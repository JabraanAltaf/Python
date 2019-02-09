#Altaf_Jabraan-CA06
#201275442
#November 2017
# Creating a program which translates Morse Code in to English, while outputting a dictionary of english letters and their Morse equivalent. This program will also join two lists together of Numbers (0-9) and their Morse Code equivalent and create a dictionary which will be outputted in reverse order.

#Sources used to help:
#http://www.geeksforgeeks.org/morse-code-translator-python/ helped with translation 

# Original Morse Code without vowels
OriginalMorse = {'B':'-...',
	         'C':'-.-.',
                 'D':'-..',
	         'F':'..-.',
                 'G':'--.',
                 'H':'....',
                 'J':'.---',
                 'K':'-.-',
	         'L':'.-..',
                 'M':'--',
                 'N':'-.',
	         'P':'.--.',
                 'Q':'--.-',
	         'R':'.-.',
                 'S':'...',
                 'T':'-',
	         'V':'...-',
                 'W':'.--',
	         'X':'-..-',
                 'Y':'-.--',
                 'Z':'--..'}
#--------------------------------------------------------------------------------------------------------------------------------------------------
#EXTENDED REQUIREMENT
def numberReverse():
   print ("\n")
   start = input("Do you want to display the Morse Code of Numbers? (Y/N): ")
   start = start.upper()
   if start == "N":
      mainmenu()
   if start == "Y":
    print ("Morse Code for Numbers in order 9-0")
    numList = ("0","1","2","3","4","5","6","7","8","9")
    morseList = ("---",".----","..---","...--","....-",".....","-....","--...","---..","----.")

    #Zip function allows us to join both the Number List and the equivalent Morse Code List together to create a dictionary)
    zippedList = list(zip(numList, morseList))


    dictionary= dict(zippedList)
    for k in sorted(dictionary,reverse=True): # Iterates keys to sort the numbers in numberical order but in reverse
      print(k,dictionary[k]) #Prints out this column of numbers in reverse from 9 to 0     
#--------------------------------------------------------------------------------------------------------------------------------------------------
def dictChange():
   FullMorse = {'B':'-...',
	        'C':'-.-.',
                'D':'-..',
	        'F':'..-.',
                'G':'--.',
                'H':'....',
                'J':'.---',
                'K':'-.-',
	        'L':'.-..',
                'M':'--',
                'N':'-.',
	        'P':'.--.',
                'Q':'--.-',
	        'R':'.-.',
                'S':'...',
                'T':'-',
	        'V':'...-',
                'W':'.--',
	        'X':'-..-',
                'Y':'-.--',
                'Z':'--..'}
#Adding vowels and their Morse Code equivalent to a new dictionary based of the original
   FullMorse["A"] = '--' 
   FullMorse["E"] = '.'
   FullMorse["I"] = '..'
   FullMorse["O"] = '---'
   FullMorse["U"] = '..-'

   return FullMorse #returns the new morse code
#--------------------------------------------------------------------------------------------------------------------------------------------------
def output():
    start = input("Do you want to display the Morse Code Dictionaries? (Y/N): ")
    start = start.upper()
    if start == "N":
       mainmenu()
    if start == "Y":
     Original = OriginalMorse
     print ("\n\n")
     print ("Original Morse Code Book (Random Order): ") #Printing out the original Morse Code in a random order
     for j in Original:
       print (j,Original[j]) # Prints the original Morse Code in random order in a column

     print("\n\n\n") 
     dic = dictChange() # Get's the new Morse Code Dictionary (with vowels) from dictChange() function
     print("Updated Morse Code Book with vowels (English Alphabetical Order)")

     for i in sorted(dic): # Sorted function orders letters to be in alphabetical order
      print(i,dic[i]) #Prints out the new Morse Code dictionary in alphabetical order and in a column 

    numberReverse() # Goes to the Numbers reverse function
#--------------------------------------------------------------------------------------------------------------------------------------------------
def decrypt(code):

	code += " " #adds an extra space at the end of the code to get the last morse code
	decipher = ""  # Will store the decrypted code
	characters = '' # Will store the morse code characters
	for letter in code: #When the letters are in the code
		# checks for when there is a space
		if (letter != ' '):
			# A counter is used to keep track of number of spaces
			i = 0
			# stores morse code of a character
			characters += letter
		# in case of space
		else:
			# i = 1 shows that there is a new morse code character as there is only one space
			i += 1
			# if i = 2 it would show a new word as there would be two spaces between the morse code characters
			if i == 2 :
				# adding space to separate words
				decipher += " "
			else:

				# Gets the equivalent keys(letters) using the values (Morse Code Characters) and adds them to 'decipher'
				decipher += list(OriginalMorse.keys())[list(OriginalMorse
				.values()).index(characters)] #index helps access the elements within the character lists
				characters = ''
	return decipher
# Function which will display translated Morse Code in to English
def translate():
 message = ".-- .... -.--  .-.. -.-- -. -..-  -.-. .-. -.--"
 print ("\n")
 print ("Morse Code Received: ",message) # Will print out the Morse Code
 english = decrypt(message) #Accesses 'decipher' from the function above which gets the translated Morse Code
 print ("\n")
 print ("Translating Morse Code...")
 print ("\n")
 print ("Code is: ",english) #Prints out translated Morse Code

 output()
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Function for Main Menu
def mainmenu(): 
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

    if option == "B":
      translate() #loads up starting prompt
      
mainmenu()
