from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'The GOAL',
        'name': 'Arisa Raezzura Zahra',
        'class': 'PBD KKI'
    }

    return render(request, "main.html", context)