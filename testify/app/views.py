from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def your_view(request):
    if request.method == 'POST':
        your_data = request.POST.get('your_field')
        print("kys: ", your_data)
        return HttpResponse('Data received successfully.')
    return render(request, 'index.html')


""" function to new html

def my_account(request):
    return render(request, "app/my_account.html")

def my_test(request):
    return render(request, "app/my_test.html")

def new_test(request):
    return render(request, "app/new_test.html")

def privacy_policy(request):
    return render(request, "app/privacy_policy.html")

def terms_of_service(request):
    return render(request, "app/terms_of_service.html")

def contact(request):
    return render(request, "app/contact.html")

"""