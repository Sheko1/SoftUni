from django.shortcuts import render, redirect

# Create your views here.
from core.profile_utils import get_profile
from expenses_tracker.expenses_tracker_app.forms import CreateProfileForm, CreateExpenseForm, EditExpenseForm, \
    DeleteExpenseForm, EditProfileForm
from expenses_tracker.expenses_tracker_app.models import Expense


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)


def home_page(request):
    profile = get_profile()

    if not profile:
        return create_profile(request)

    expenses = Expense.objects.all()

    context = {
        'profile': profile,
        'expenses': expenses,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = CreateExpenseForm()

    context = {
        'form': form
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'form': form,
        'expense': expense
    }

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        expense.delete()
        return redirect('home page')

    context = {
        'form': DeleteExpenseForm(instance=expense),
        'expense': expense,
    }

    return render(request, 'expense-delete.html', context)


def profile_page(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile page')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        profile.delete()
        Expense.objects.all().delete()
        return redirect('home page')

    return render(request, 'profile-delete.html')
