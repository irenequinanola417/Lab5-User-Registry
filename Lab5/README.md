## User Registry Program

This is a console-based User Registry program written in Python.

The program allows the user to:
- Add a user
- List all users
- Search by username
- Exit the program


## How to Run the Program

1. Open terminal or command prompt
2. Navigate to the Lab5 folder
3. Run the following command:

python main.py


## Validation Rules Used

Username:
- Must be unique
- Stored in a set to prevent duplicates

Full Name:
- Cannot be blank
- .strip() is used to remove spaces

Age:
- Must be numeric
- Must be between 13 and 120
- Converted from string to integer after validation

Email:
- Must contain '@' and '.'
- Basic format validation only


## Data Structures Used

List:
- Used to store all user dictionaries

Dictionary:
- Each user is stored as a dictionary with:
  - username
  - full_name
  - age
  - email

Set:
- Used to store usernames for fast uniqueness checking


## Why List + Dictionary + Set?

A list is used to store multiple users.
A dictionary is used to organize each user’s data clearly.
A set is used to efficiently prevent duplicate usernames.
