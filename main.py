import os
print("Текущая рабочая директория:", os.getcwd())

filename = r"C:\Users\iratk\OneDrive\Рабочий стол\files\cookbook.txt"

def read_cook_book(filename):
    cook_book = {}

    with open(filename, encoding='utf-8') as file:
        file_lines = file.read().strip().split('\n')

        i = 0
        while i < len(file_lines):
            if file_lines[i].strip() == '':
                i += 1
                continue

            dish_name = file_lines[i]
            ingredients_count = int(file_lines[i + 1])
            ingredients = []

            for j in range(ingredients_count):
                ingredient_line = file_lines[i + 2 + j].split('|')
                ingredient_name = ingredient_line[0].strip()
                quantity = int(ingredient_line[1].strip())
                measure = ingredient_line[2].strip()

                ingredients.append({'ingredient_name': ingredient_name,
                                   'quantity': quantity,
                                   'measure': measure})

            cook_book[dish_name] = ingredients
            i += 2 + ingredients_count

    return cook_book

cook_book = read_cook_book(filename)

for dish, ingredients in cook_book.items():
    print(f'{dish}: {ingredients}')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list

result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

for ingredient, details in result.items():
    print(f'{ingredient}: {details}')








