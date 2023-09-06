'''Домашнее задание №1'''


def main():
    
    def activities(age):
      
      try:  
        
        age = int(age)
        
        if age < 3:
          activity = "Еще рано ходить в детский сад"
          
        elif 3 <= age <= 6:
          activity = "Ходить в детский сад"
        
        elif 7 <= age <= 17:
          activity = "Ходить в школу"
          
        elif 18 <= age <= 23:
          activity = "Учиться в ВУЗе"
        
        elif 23 <= age <= 65:
          activity = "Пенсия"
        
        return activity
        
      except ValueError:
        print("Вам нужно ввести число")
        
      
    
    
    age = input("Введите ваш возраст: ")
    suitable_activity = activities(age)
    print(suitable_activity)
    
    pass
  


if __name__ == "__main__":
    main()
