from django.shortcuts import render


def profile(request, username):
    context = {
        "username": username
    }
    return render(request, 'users/profile.html', context)
