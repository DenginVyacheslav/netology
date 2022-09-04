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






