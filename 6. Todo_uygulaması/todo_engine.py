show_items_option = "1"
add_items_option = "2"
finish_item_option = "3"
exit_option = "4"

todo_list = {}


def show_menu():
    menu_text = "1. Listeyi göster \n2. Listeye görev ekle \n3. Görevi tamamla \n4. Çıkış"
    return input(menu_text)


def show_items():
    item_index = 1
    for name in todo_list.keys():
        status_text = "Yapıldı"
        if todo_list[name]:
            status_text = "Yapdıldı"
        print(item_index, ". Görev : ", name, ", Durumu : ",status_text)
        item_index +=1

def add_item():
    item_text = input("Görevi giriniz : ")
    todo_list[item_text] = False


def finish_item():
    item_index = int(input("Görev numarasını giriniz : "))
    for name in todo_list.keys():
        item_index -= 1
        if todo_list == 0:
            todo_list[name] = True
            break


def print_message(message):
    print(message)
