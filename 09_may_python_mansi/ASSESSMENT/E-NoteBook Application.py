
import datetime # imports the datetime module for show present date and time

import os # imports the os module




def display_menu(): # create this function for display the main menu for the Python E-Note program.
	print("\t\tWelcome To Python E-Note\n")#print welcome message
	print("\t\tPress 1 for Generate Note")# print message for user press 1 to generate a note.
	print("\t\tPress 2 for View Note")# print message user press 2 for view notes.
	print("\t\tPress 4 for Exit\n\n")#print 4 to exit from e-book
	print("Enter your choice: ")#take choice from the user 

'''
when user select option 1 then accept following details from user 
'''

def generate_note():
	print("Enter Python E-Note Generator Name:") #ask user to  their choice
	generator_name = input()# take user input and storeit in generator_name variable.
	while not generator_name:# while loop for continue this line and stop only when user input right choice.
		print("Invalid input. Please enter a valid name.")#this message will show to user if user enter without write anything or left it empty
		generator_name = input()# after that again ask user for input 
	
	print("Enter Python E-Note Book Title:")#if user enter a valid name after that show this message to user in screen to ask them their book title
	title = input()#take input from the user nd store it in enter python E- Book title 
	while not title:#start while loop to countinue untill user enter input not left it empty.
		print("Invalid input. Please enter a valid title.")#show this message if user enter without write anything in it and left it empty.
		title = input()#again ask user for input
	
	print("Enter E-Note Content:")#if user enter title than after show this message for asking title content
	content = input() #take a varibale name content to store what user write in this 
	while not content:#again start a while loop and countine loop untill user input something 
		print("Invalid input. Please enter some content.")#if user left it empty then show this message to user.
		content = input()#and again ask user to input content 
	
	with open("notes.txt", "a") as file:#after that open a file called "notes.txt" in append mode.
		file.write(f"-----------\n{datetime.datetime.now()}\nE-Note title: {title}\nE-note Description: {content}\nNote Generator: {generator_name}\n---------------------------\n")
	#file.write(...) -> in this line write note to file, with  present date and time, title, content, and generator name.

	print("Note saved successfully!")#show this message to user after note saved.  

def view_note():#create a function for show all notes that are saved.

	with open("notes.txt", "r") as file:# open notes.txt in read mode. r for read mode
		print(file.read())#to print read  file take print function.

def log_transaction(message):#will log a message to a file.
	with open("log.txt", "a") as file:#open file log.txt in append mode.
		file.write(f"{datetime.datetime.now()}: {message}\n")#This line writes a message to a file with a timestamp.
		#datetime.datetime.now() gets the current date and time. f-string formatting is used to insert the timestamp and message into a string.
		# #\n adds a newline character to the end of the string.
def main():#This defines a function named main.
	display_menu()#   - This calls a function named display_menu (not shown in this code snippet).
    #It likely displays a menu to the user
	while True:#This starts an infinite loop that will continue until the program is exited.
		choice = input()#his gets user input (a choice) from the console.
		if choice == "1":#This checks if the user chose option 1.
			generate_note()#This calls a function named generate_note (not shown in this code snippet).
    	#It likely generates a new note.
			log_transaction("Note generated")#This calls a function named log_transaction (not shown in this code snippet).
    									#It logs a transaction with a message ("Note generated").	
			display_menu()#This calls the display_menu function again to show the menu.
		elif choice == "2":#This checks if the user chose option 2.
			view_note()#This calls a function named view_note (not shown in this code snippet).
    			#It likely views an existing note.
			log_transaction("Note viewed")#This logs a transaction with a message ("Note viewed").
			display_menu()#This calls the display_menu function again to show the menu.
		elif choice == "4":#This checks if the user chose option 4 (likely an exit option).
			break#This exits the infinite loop.
		else:#This catches any other invalid choices.
			print("Invalid choice. Please try again.")#This prints an error message to the console.
			log_transaction("Invalid choice")#This logs a transaction with a message ("Invalid choice").
			display_menu()#This calls the display_menu function again to show the menu.

if __name__ == "__main__":#This calls the display_menu function again to show the menu.
	main()#his calls the main function to start the program.
