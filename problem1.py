#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people = ["Crow", "Shelly", "Dina", "Spike", "Buster", "Amber"]
print(people)
Rework = input("Enter a name from the list to replace: ")
people.remove(Rework)
NewBrawler = input("Enter a name for the new brawler: ")
people.insert(0, NewBrawler)
print(people)