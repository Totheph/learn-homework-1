"""

Домашнее задание №1

Условный оператор: Сравнение строк

"""

def main():
    
    
  def strings(str_1, str_2):
    
    if type(string_1) == str and type(string_2) == str:
      if string_1 == string_2:
        return 1
        
      elif string_2 == "learn":
        return 3
        
      elif len(string_1) > len(string_2):
        return 2
      
      else: #в условии нет про возвращение 4, но мне показалось, что возвращение хоть какого-то значения должно быть при несоответствии всем условиям
        return 4

    else:
      return 0
    
  
  string_1, string_2 = input(), input()
  print(strings(string_1, string_2))
    
if __name__ == "__main__":
    main()
