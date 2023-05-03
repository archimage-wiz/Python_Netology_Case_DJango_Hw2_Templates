from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calculator(request, receipe_name):
    receipe_data = DATA.get(receipe_name)
    if not receipe_data:
        return render(request, 'calculator/index.html')
    receipe_data = receipe_data.copy()
    receipe_multiply = int(request.GET.get("servings", 1))
    receipe_multiply = 1 if receipe_multiply < 1 or receipe_multiply > 65535 else receipe_multiply
    for item in receipe_data:
        receipe_data[item] = receipe_data[item] * receipe_multiply
    context = {
        'recipe': receipe_data
    }
    return render(request, 'calculator/index.html', context)
