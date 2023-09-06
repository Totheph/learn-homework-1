"""

Домашнее задание №1

Цикл for: Продажи товаров
"""

from functools import reduce

def main():
    
  def products(product_list):
    for product in goods:
      summ_product = sum(product["items_sold"])
      average_product = sum(product["items_sold"]) / len(product["items_sold"])
      
      print(f"Суммарное количество продаж товара {product['product']}: {summ_product}", f"Среднее количество продаж товара {product['product']}: {average_product}", sep = "\n")
      
    summ_all_products = sum(reduce(lambda x, y: x + y, (product["items_sold"] for product in goods)))
    
    average_all_products = summ_all_products / len(reduce(lambda x, y: x + y, (product["items_sold"] for product in goods)))
      
    print(f"Суммарное количество продаж всех товаров {summ_all_products}",
    f"Среднее количество продаж всех товаров {average_all_products}", sep ="\n")
  
  
      
  goods = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]    
  
  products(goods)
  
  
  
if __name__ == "__main__":
    main()
