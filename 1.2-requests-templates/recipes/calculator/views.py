from django.http import HttpResponse
from django.shortcuts import render, reverse

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
def home_view(request):
    # Список всех блюд
    template_name = 'calculator/recipe.html'
    pages = {}
    for key in DATA.keys():
        pages[key] = key

    context = {
        'pages': pages
    } 
    return render(request, template_name, context)

def recipe_view(request, recipe_name):
    # Расчет количества ингридиентов. 
    # Для расчета нескольких порций добавить ?servings=<количество> в адресную строку
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    dish = {}
    if recipe_name in DATA:
        for ingredient, amount in DATA[recipe_name].items():
            dish[ingredient] = round(amount * servings, 1)
    context = {'recipe': dish}
    return render(request, template_name, context)

