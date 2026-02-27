# Lab 5 - User Registry Program
# Age rule: 13–120
# Email rule: must contain "@" and "."
# Username must be unique

users = []              # list of dictionaries
usernames = set()       # set for unique usernames


def get_valid_username():
    while True:
        username = input("Enter username: ").strip()

        if username == "":
            print("Username cannot be blank.")
        elif username in usernames:
            print("Username already exists. Please choose another.")
        else:
            return username


def get_valid_fullname():
    while True:
        full_name = input("Enter full name: ").strip()

        if full_name == "":
            print("Full name cannot be blank.")
        else:
            return full_name


def get_valid_age():
    while True:
        age_input = input("Enter age: ").strip()

        if not age_input.isdigit():
            print("Age must be a number.")
        else:
            age = int(age_input)

            if age < 13 or age > 120:
                print("Age must be between 13 and 120.")
            else:
                return age


def get_valid_email():
    while True:
        email = input("Enter email: ").strip()

        if "@" not in email or "." not in email:
            print("Invalid email format. Must contain '@' and '.'.")
        else:
            return email


def add_user():
    print("\n--- Add User ---")

    username = get_valid_username()
    full_name = get_valid_fullname()
    age = get_valid_age()
    email = get_valid_email()

    user = {
        "username": username,
        "full_name": full_name,
        "age": age,
        "email": email
    }

    users.append(user)
    usernames.add(username)

    print("User added successfully!\n")


def list_users():
    print("\n--- All Users ---")

    if len(users) == 0:
        print("No users found.\n")
    else:
        for user in users:
            print(f"Username: {user['username']}")
            print(f"Full Name: {user['full_name']}")
            print(f"Age: {user['age']}")
            print(f"Email: {user['email']}")
            print("------------------------")
        print()


def search_user():
    print("\n--- Search User ---")

    search_name = input("Enter username to search: ").strip()

    if search_name in usernames:
        for user in users:
            if user["username"] == search_name:
                print("User found:")
                print(f"Full Name: {user['full_name']}")
                print(f"Age: {user['age']}")
                print(f"Email: {user['email']}")
                print()
                break
    else:
        print("User not found.\n")


def main():
    while True:
        print("==== User Registry Menu ====")
        print("1. Add User")
        print("2. List All Users")
        print("3. Search by Username")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            search_user()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.\n")


if __name__ == "__main__":
    main()
