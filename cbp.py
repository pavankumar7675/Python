import time
import os

class User:
    def __init__(self, name='', username='', password='', address=''):
        self.name = name
        self.username = username
        self.password = password
        self.address = address

new_user = User()

items = []
costs = []
quantities = []

def login_user():
    username = input("\nEnter username: ")
    password = input("Enter password: ")

    try:
        with open("usersnew.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                user = User(lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip(), lines[i + 3].strip())
                if username == user.username and password == user.password:
                    print("\n\n")
                    display_menu()
                    return True
        print("\nInvalid username or password!\n\n\n")
        return False
    except FileNotFoundError:
        print("Error opening file!\n")
        return False

def register_user():
    global new_user

    new_user.name = input("\nEnter name: ").strip()
    new_user.username = input("Enter username: ").strip()
    new_user.password = input("Enter password: ").strip()
    new_user.address = input("Enter address: ").strip()

    with open("usersnew.txt", "a") as file:
        file.write(f"{new_user.name}\n{new_user.username}\n{new_user.password}\n{new_user.address}\n")

    print("Registration successful!\n\n")
    display_menu()

def display_menu():
    global items, costs, quantities

    current_hour = time.localtime().tm_hour

    while True:
        if 5 < current_hour <= 12:
            print("Good morning\n-----menu-----\n1) Dosa\n2) Idly\n3) Vada\n4) Bonda\n")
            menu = [("Dosa", 80), ("Idly", 50), ("Vada", 60), ("Bonda", 70)]
        elif 12 < current_hour < 17:
            print("Good afternoon\n-----Menu-----\n1) Biryani\n2) Fried rice\n3) Chicken Biryani\n4) Rice with curries\n")
            menu = [("Biryani", 200), ("Fried rice", 150), ("Chicken Biryani", 300), ("Rice with curries", 80)]
        else:
            print("Good Evening\n-----Menu-----\n1) Biryani\n2) Naan\n3) Cake\n4) Samosa\n")
            menu = [("Biryani", 200), ("Naan", 100), ("Cake", 150), ("Samosa", 50)]

        choice = int(input("Enter choice: "))
        qty = int(input("Enter quantity: "))

        if 1 <= choice <= 4:
            item, cost = menu[choice - 1]
            items.append(item)
            costs.append(cost)
            quantities.append(qty)
        else:
            print("Invalid choice!")

        print("\n\nYour order summary:\n")
        for i in range(len(items)):
            print(f"{i + 1}) {items[i]} - Quantity: {quantities[i]}, Cost: {costs[i]}")

        final_cost = sum(q * c for q, c in zip(quantities, costs))
        print(f"\nFinal Cost: {final_cost}\n\n")

        cont = int(input("Enter\n1.To continue\n2.Exit\n"))
        if cont == 2:
            break

    checkout()

def checkout():
    global new_user

    print("\nOrder Summary:\n")
    for i in range(len(items)):
        print(f"{i + 1}) {items[i]} - Quantity: {quantities[i]}, Cost: {costs[i]}")

    final_cost = sum(q * c for q, c in zip(quantities, costs))
    print(f"\nFinal Cost: {final_cost}\n\n")

    upi = input("Enter UPI pin: ")
    otp = input("Enter OTP: ")

    print("Processing payment...\n")
    time.sleep(2)
    print("Payment successful!\n")

    new_user.address = input("Enter delivery location: ").strip()
    print(f"\nOrder confirmed! Your order will be delivered to {new_user.address}.\n")
    exit(0)

def main():
    while True:
        print("\n------------ BiteBuddy ------------\n1. Login\n2. Register\n3. Exit\n")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            if login_user():
                print("Welcome to BiteBuddy! Have a great day!")
        elif choice == 2:
            ch = input("Register Now\nIf you have already registered enter 'y' else 'n': ").strip().lower()
            if ch == 'y':
                login_user()
            else:
                register_user()
        elif choice == 3:
            exit(0)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
