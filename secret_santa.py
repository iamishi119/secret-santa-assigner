import random

users = {}
participants = []
assignments = {}
draw_locked = False


def signup():
    username = input("Enter username: ")

    if username in users:
        print("User already exists!")
        return

    password = input("Enter password: ")

    wishlist = input("Enter your wishlist: ")

    users[username] = {
        "password": password,
        "wishlist": wishlist
    }

    participants.append(username)

    print("Signup successful!")


def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username

    print("Invalid credentials!")
    return None


def generate_assignments():
    global assignments
    global draw_locked

    if len(participants) < 2:
        print("Need at least 2 participants.")
        return

    shuffled = participants[:]

    while True:
        random.shuffle(shuffled)

        valid = True

        for i in range(len(participants)):
            if participants[i] == shuffled[i]:
                valid = False
                break

        if valid:
            break

    assignments = {}

    for i in range(len(participants)):
        assignments[participants[i]] = shuffled[i]

    draw_locked = True

    print("Secret Santa draw completed!")


def reveal_giftee(username):

    if username not in assignments:
        print("Draw has not been run yet.")
        return

    giftee = assignments[username]

    print("\nYour Giftee:", giftee)
    print("Wishlist:", users[giftee]["wishlist"])


def view_all_users():
    print("\nRegistered Users:")
    for user in participants:
        print(user)


while True:

    print("\n===== SECRET SANTA SYSTEM =====")
    print("1. Signup")
    print("2. Login")
    print("3. Run Draw")
    print("4. View Users")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        if draw_locked:
            print("Draw already completed. No new signups allowed.")
        else:
            signup()

    elif choice == "2":

        user = login()

        if user:
            while True:

                print("\n--- User Menu ---")
                print("1. Reveal My Giftee")
                print("2. Logout")

                sub_choice = input("Enter choice: ")

                if sub_choice == "1":
                    reveal_giftee(user)

                elif sub_choice == "2":
                    break

                else:
                    print("Invalid choice.")

    elif choice == "3":
        generate_assignments()

    elif choice == "4":
        view_all_users()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")