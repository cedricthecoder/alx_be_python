shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    global shopping_list
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for adding an item
            new_item_name = input("Enter the item to add: ")
            shopping_list.append(new_item_name)
            print(f"The new shopping list is: {shopping_list}")
            pass
        
        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove =input("Enter item to remove:")
            
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"The new shopping list: {shopping_list}")
            else:
                print(f"The item {item_to_remove} is not found in the shopping list.")
            pass
        
        elif choice == '3':
            # Display the shopping list
            print(f"The list is: {shopping_list}")
            pass
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    main()

