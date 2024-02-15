from quiz import *

def show_status():
    print("Toplam sorulan soru sayısı = ", total_asked_questions)
    print("Toplam doğru bilinen soru sayısı = ", total_correct_questions)

while True:
    choice = show_menu()

    if choice == option_ask:
        question = questions[total_asked_questions]
        total_asked_questions += 1
        if assess_question(question):
            total_correct_questions += 1
    elif choice == option_exit:
        break

show_status()