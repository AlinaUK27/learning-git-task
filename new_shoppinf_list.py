print("HOWDY")

print("CПИСОК ПОКУПОК")
shopping_dict = {"пекарня":['хліб', 'булочки', 'пончик'],
"продуктовий": ['морква', 'селера', 'рукола']
}
 
for keys, values in shopping_dict.items():
    print(f"Заходжу в {keys.title()}, купую тут такі товари:{values.__str__().title()}")
value1 = shopping_dict["пекарня"]
value2 = shopping_dict["продуктовий"]
print(f"Разом купую {len(value1) + len(value2)} товарів")

del shopping_dict ["продуктовий"]

shopping_dict ["пекарня"] = ['лаваш', 'печиво']

new_shopping_dict = shopping_dict.copy()
new_shopping_dict ["будівельний"] = ["фарба жовта", "фарба блакитна", "пензлі"]

for keys, values in new_shopping_dict.items():
    print(f"Я йду до {keys.title()} та купую там:{values.__str__()}") 

value3 = new_shopping_dict["пекарня"]
value4 = new_shopping_dict["будівельний"]
total = len(value3) + len(value4)
print(f"Всього я разом купую {total} товарів")

new_shopping_dict ["тканини"] = ["гудзики", "нитки білі"]

for keys, values in new_shopping_dict.items():
    print(f"Я йду до {keys.title()} та купую там:{values.__str__()}") 

value5 = new_shopping_dict["тканини"]
total = len(value3) + len(value4) + len(value5)
print(f"Всього я разом купую {total} товарів")







