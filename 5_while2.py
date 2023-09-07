"""

Домашнее задание №1

Цикл while: ask_user со словарём

"""

questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Откуда ты?": "Из России", "Как тебя зовут?": "Совесть", "Сколько тебе лет?": "Много", "Ты работаешь?": "Каждый день", "Любишь Python": "Люблю"}

def ask_user(answers_dict):
  while True:
    question = input("Задайте свой вопрос: ")
    print(questions_and_answers.get(question, "Мы не можем ответить на ваш вопрос"))
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
