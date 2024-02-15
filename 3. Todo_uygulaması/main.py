from todo_engine import *

print_message("ToDo programına hoş geldiniz")


while True:
    choice = show_menu()

    if choice == show_items_option:
        show_items()
    elif choice == add_items_option:
        add_item()
    elif choice == finish_item_option:
        finish_item()
    elif choice == exit_option:
        break
    else:
        print_message("Böyle bir işlem yok")

print_message("Program bitti")