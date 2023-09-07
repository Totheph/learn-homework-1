"""

Домашнее задание №1

Исключения: KeyboardInterrupt

    
"""

def hello_user():
  while True:
    try:
      answer = input("Как дела?")
      if answer == "Хорошо":
        break
    except KeyboardInterrupt:
      print("Пока!")
      break
    
    
if __name__ == "__main__":
    hello_user()
