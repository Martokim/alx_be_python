

def display_menu():
    print("\nShopping List Manager:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #prompt for and add an item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Added {item} to the shopping list.")
        elif choice == '2':
            #prompt for and remove an item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed {item} from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")
        elif choice == '3':
            #display the current shopping list
            if not shopping_list:
                print("The shopping list is currently empty.")
            print("Current Shopping List:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        elif choice == '4':
            print("Exiting the Shopping List Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
