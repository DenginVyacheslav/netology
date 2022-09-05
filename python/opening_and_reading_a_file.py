import random
# Задание 1

def file_processing(l1, l2):
    new = []
    n1 = 0
    n2 = 0
    book = {}
    tmp = ['ingredient_name', 'quantity', 'measure']
    for i, k in enumerate(l2):
        if i % 2 == 0:
            name = k
        if i % 2 != 0:
            n2 += int(k)
            for ing in l1[n1:n2]:
                new.append(dict(zip(tmp, ing)))
            n1 = n2
            book[name] = list(new)
        new.clear()
    return book

def get_shop_list_by_dishes(ld, p):
    ingred = []
    name_ingred = []
    ingred2 = []

    for name in ld:
       for v in cook_book[name]:
          for k, g in v.items():
              if k == 'ingredient_name':
                 name_ingred.append(g)
              if k == 'measure':
                  ingred.append(g)
              if k == 'quantity':
                  ingred2.append(int(g) * p)

    menu = {}
    for n, v in enumerate(name_ingred):
      menu[v] = {'measure':ingred[n], 'quantity':ingred2[n]}

    return menu

name_of_dishes = []
ingredient =[]

with open('recipes.txt', encoding='utf-8') as f:
    for line in f:
        if '|' in line:
            ingredient.append(line.strip().split('|'))
        else:
            if line != '\n':
                name_of_dishes.append(line.strip())

cook_book = file_processing(ingredient, name_of_dishes)


for k, v in cook_book.items():
    print(k, v)

print('\n======================================\n')
# Задание 2
person_count = random.randint(1, 5)
dishes = cook_book.keys()

person = get_shop_list_by_dishes(dishes, person_count)

for k, v in person.items():
    print(k, ":", v)


