# main.py

from modules import student_phonebook, clean_data, visualize

def main():
    """
    Main menu for the Student Project.
    Allows user to:
    1. Manage phonebook (add/read/delete students)
    2. Clean dataset
    3. Visualize data
    4. Exit
    """
    while True:
        print("\n=== STUDENT PROJECT MENU ===")
        print("1. Phonebook System")
        print("2. Clean Dataset")
        print("3. Visualize Data")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            # Launch phonebook menu
            student_phonebook.menu()
        elif choice == "2":
            # Launch dataset cleaning operations
            if hasattr(clean_data, "clean_dataset"):
                clean_data.clean_dataset()
            else:
                print("⚠️ clean_dataset() not implemented in clean_data.py")
        elif choice == "3":
            # Launch visualization
            if hasattr(visualize, "plot_graphs"):
                visualize.plot_graphs()
            else:
                print("⚠️ plot_graphs() not implemented in visualize.py")
        elif choice == "4":
            print("Exiting Student Project. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
