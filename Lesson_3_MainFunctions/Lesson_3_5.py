import random

dictionary = {"Hello": "Здравствуй", "Bye": "Пока", "Lesson": "Урок"}
done = False

while not done:

    ang_key = random.choice(list(dictionary.keys()))    # получаю случайное значение из словаря
    rus_value = dictionary[ang_key]

    while True:     # бесконечный цикл
        anginput = input("Введите перевод на английском для слова " + rus_value + ":")
        # if ang_key.lower()==anginput:
        if anginput.lower() == "quit":
            done = True
            break
        if anginput.lower() == "show":
            print(dictionary)
        elif ang_key.lower() == anginput.lower():
            break
        else:
            print("Ответ не верный!!!")
