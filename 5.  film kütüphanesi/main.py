from screen_support import *
from movie_engine import *


print_message("Film kütüphanesi v1.0")
while True:
    choice = show_menu()

    if choice == option_show_list:
        show_movies()
    elif choice == option_add_movie:
        add_movie()
    elif choice == option_delete_movie:
        delete_movie()
    elif choice == option_exit:
        break
    else:
        print_message("Böyle işlem bulunamamkta")

print_message("Program bitti")