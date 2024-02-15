# Proje <br/><br/>

# 1. projede kullandığım dil
# 2. Projenin amacı
# 3. Projemde olan uygulmalar
# 4. Her projeden birkaç örnek<br/><br/><br/>

# 1. Projemde kullandığım dil
## Python.<br/><br/><br/>

# 2. Projenin amacı
## Projemin amacı insanlara yaptığım uygulamaları göstermek ve onlarında benim kod bloklarımdan esinlenip daha iyi bir şekilde kod yazmalarıdır.<br/><br/><br/>

# 3. Projemde olan uygulamalar
## 1. Zar atma uygulması.
## 2. Taş Kağıt Makas uygulaması.
## 3. Todo listesi.
## 4. Quiz.
## 5. Film kütüphanesi uygulması.<br/><br/><br/>

# 4. Her projeden birkaç örnek
## Zar atma uygulması
``` python
def roll_dice(quantity):
    for i in range(quantity):
        roll = random.randint(1, 6)
        roll_list.append(roll)
        print("Attığınız zar :", roll, "geldi")
```

## Taş kağıt makas uygulaması
``` python
def play_game():
    get_computer_choice()
    
    if gamer_choice == computer_choice:
        print("berabere")
    elif gamer_choise_rock:
        if computer_choise_paper:
            print("Bilgisayar kazandı")
        else:
            print("Kazandınız")
    elif gamer_choise_paper:
        if computer_choise_sciss:
            print("Bilgisayar kazandı")
        else:
            print("Kazandınız")
    elif gamer_choise_sciss:
        if computer_choise_rock:
            print("Bilgisayar kazandı")
        else:
            print("kazandınız")
```

##  Todo listesi
``` python
def show_items():
    item_index = 1
    for name in todo_list.keys():
        status_text = "Yapıldı"
        if todo_list[name]:
            status_text = "Yapdıldı"
        print(item_index, ". Görev : ", name, ", Durumu : ",status_text)
        item_index +=1
```

## Quiz
``` python
def assess_question(question):
    print(question["question_text"])
    answer = input(question["answer"])
    correct_answer = question["correct_answer"]
    if answer == correct_answer:
        return True
```

## Film Kütüphanesi
``` python
def add_movie():
    name = get_name()
    director = get_director()
    year = get_year()
    key = len(movies.items()) +1
    movies[key] = {"movie_name": name, "movie_director": director, "movie_year": year}
```