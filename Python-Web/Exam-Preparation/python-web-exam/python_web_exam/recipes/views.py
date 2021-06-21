from django.shortcuts import render, redirect

# Create your views here.
from python_web_exam.recipes.forms import RecipeForm
from python_web_exam.recipes.models import Recipe


def disable_form_fields(form):
    for field in form.fields:
        form.fields[field].disabled = True

    return form


def show_recipe_form(request, form, template_name):
    context = {
        'form': form
    }

    return render(request, template_name, context)


def index(request):
    recipes = sorted(Recipe.objects.all(), key=lambda x: x.id)

    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    form = RecipeForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

        return show_recipe_form(request, form, 'create.html')

    return show_recipe_form(request, RecipeForm(), 'create.html')


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('index')

        return show_recipe_form(request, form, 'edit.html')

    form = RecipeForm(initial=recipe.__dict__)

    return show_recipe_form(request, form, 'edit.html')


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        recipe.delete()
        return redirect('index')

    form = RecipeForm(initial=recipe.__dict__)
    form = disable_form_fields(form)

    return show_recipe_form(request, form, 'delete.html')


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }

    return render(request, 'details.html', context)
