print("Добро пожаловать в квиз по знанию Японской культуре!")
print("Ответь на следующие вопросы: ")

score = 0

questions = [
    "как называется народный костюм Японии?",
    "Как называется праздник любования сакурой?",
    "Самое популярное блюдо в Японии?",
    "В каком году основалась Япония?",
    "Что было изобретено в Японии?",
    "Как называется каллиграфия в Японии?",
    "Сколько алфавитов в Японии?",
    "У какого языка Япония позаимствовала иероглифы?"
]
answers = [
    "Кимоно",
    "Ханами",
    "Мисо суп",
    "660 д.н.э.",
    "DVD диски",
    "Сёдо",
    "3",
    "Китай"
]

print(questions[0])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[0].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[1])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[1].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[2])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[2].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[3])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[3].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[4])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[4].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[5])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[5].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[6])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[6].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print(questions[7])
user_answer = input("введи свой ответ: ")
if user_answer.lower() == answers[7].lower():
    score = score + 1
    print("правильно")
else:
    print("неправильно")

print('твой результат:', score, "баллов из", len(questions))
if score >= 7:
    print("Это отличный результат! Ты много знаешь о культуре Японии")
elif score >= 4:
    print("Неплохой результат! Как здорово, что тебе предстоит узнать ещё так много о культуре Японии")
else:
    print("Видимо, ты только начинаешь свой путь к культуре Японии! Ты ещё много чего узнаешь о мире, где мы живём")
