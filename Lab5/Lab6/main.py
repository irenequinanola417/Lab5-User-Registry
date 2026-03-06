users = {}

def add_user():
    name = input("Enter user name: ")

    while True:
        try:
            age_input = input("Enter age: ")
            age = int(age_input)

        except ValueError:
            print("Invalid age. Please enter a number.")

        else:
            users[name] = age
            print("User added successfully.")
            break

        finally:
            print("Age input attempt finished.")

def search_user():
    name = input("Enter name to search: ")

    age = users.get(name)

    if age is not None:
        print(f"{name} is {age} years old.")
    else:
        print("User not found.")

def display_users():
    if not users:
        print("No users registered.")
        return

    for name, age in users.items():
        print(f"{name} - {age}")

def main():
    while True:
        print("\nUser Registry")
        print("1. Add User")
        print("2. Search User")
        print("3. Display Users")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            search_user()
        elif choice == "3":
            display_users()
        elif choice == "4":
            print("Program exiting.")
            break
        else:
            print("Invalid option. Try again.")

main()
