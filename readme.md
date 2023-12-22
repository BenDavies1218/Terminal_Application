# Terminal Application T1_A3
## Attributions
 - [Coding Style for python Pep8](https://pep8.org/)
 - [Subprocess module to clear terminal](https://realpython.com/python-subprocess/)

## Links
- [https://github.com/BenDavies1218/Terminal_Application](https://github.com/BenDavies1218/Terminal_Application)
- [Video Presentation]()

## Coding Style
- The coding style I have chosen for my Terminal Application is known as Pep8. Pep8 is a general coding format and a standard for developers writing modules and functions in python. Pep8 is not a set of strict rules that need to be followed but more like guidelines to making your code more readable. Pep8 stands for Python Enhancement Proposal and was written in 2001 by Guido van Rossum, Barry Warsaw and Nick Coghlan. Some of the main rules outlined in the proposal include:

    - 4 space indentation to clearly define a new indentation level
    - The maximum number of characters shouldn't exceed 79 per line for general statements and a maximum of 72 characters for comments and docstrings
    - When using binary operators such as +,-,/,* in a line that exceeds 79 characters developers should break line at a new operator
    - Functions and classes on the top level of code should have 2 blank lines separeting them
    - Methods inside a class or function should be separeted by 1 blank line
    - Imports should be done separetely for every module or package that is being imported to the file
    - Imports should always be at the top of the file
    - Developers should avoid unnessecary white space inside parenthese, brackets or braces
    - Developers should always leave white before and after using a binary operator, Comparison operator and boolean operator
    - When naming classes developers should use Pascal Case for all other names Snake case should be used
    When going about writing my code i will this set rules to ensure it is readable for myself and other developers

## Application Features
 1. Menu Feature
   - will take the players input and give an error if players name is not valid it will utilize except blocks to throw an error, also allow the user to view the game rules before they start.

      - utilize colored package to give the user a better experience
      - basic Loop
      - Control flow statements to check if input is valid
      - error handling to throw exceptions
      - write the players name to a CSV file

 2. Game Feature
   - The main Feature of the application will allow the user select a specific case and open it revealing how much money was inside. The user will be prompted if they want to accept an offer from the bank for there case. It will display the cases left to open, values remaining and value of last case open to the user, as well as how many cases need to be opened until they get another offer from the bank.

      - utilize colored package to give the user a better experience
      - advanced conditional Loops to exit the game at specific points
      - Control flow statements to check that user inputs are valid
      - error handling to throw exceptions
      - write the players game decisions to a CSV file

 3. Bank Offer Feature
   - Will calculate the offer which the user can accept or decline
    
      - utilize colored package to give the user a better experience
      - import a math package to calculate
      - accurate calculate money offer
      - test this offer to check that it works
      - write the money offer to CSV file and weather user accepted it or declined it

## Development Plan
 1. 
 2. 
 3. 

## Help Document
 - #### To run the application
  - open your terminal of choice and cd into the main directory
  - Then on the command line enter ./run.sh
  - this will then execute the bash script which will run the application

 - #### Dependencies
  - you MUST have at least python version 3 to run the application
  - I peronsally use windows for my developement and run ubuntu as my default Terminal, the application should run completely fine on all systems and terminals but some of colors may appear different or not work depending on the terminal type/version.
