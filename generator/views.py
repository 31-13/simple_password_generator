from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')


def password(request):
    characters = list('qwertyuioplkjhgfdsazxcvbnm')
    numbers = "1234567890"
    special_char = "!@#$%^&*(.,)_+"

    # check the checkbxes
    if request.GET.get('uppercase'):
        for i in range(len(characters)):
            characters.append(characters[i].upper())

    if request.GET.get('special_characters'):
        characters.extend(special_char)

    if request.GET.get('numbers'):
        characters.extend(numbers)

    # check the len
    pre_password = ""
    password_length = int(request.GET.get('length', 12))

    for x in range(password_length):
        pre_password += random.choice(characters)
    return render(request, 'password.html', {'password': pre_password})
