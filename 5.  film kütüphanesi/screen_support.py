option_show_list = "1"
option_add_movie = "2"
option_delete_movie = "3"
option_exit = "X"

def show_menu():
    menu_text = (
        option_show_list + ": Filmleri göster\n" + option_add_movie + ": Film ekle\n" + option_delete_movie + ": Film kaldır\n" + option_exit + ": Çıkış\n "
    )
    return input(menu_text)

def get_name():
    name = input("Filmin adını giriniz : ")
    return name

def get_director():
    director = input("Filmin yönetmenini giriniz : ")
    return director

def get_year():
    year = input("Filmin kaç yılında apıldığını giriniz : ")
    return year

def get_delete_movie():
    delete_movie = int(input("Silmek istediğiniz filmin numarasını giriniz : "))
    return delete_movie

def print_message(message):
    print(message)

def show_name_director_and_year(movie_key, name, director, year):
    print(f"{movie_key} => Filmin adı : {name}, Filmin yönetmeni : {director}, Filmin yapıldığı yıl : {year}")