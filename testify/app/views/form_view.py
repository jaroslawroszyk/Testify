from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def form_view(request):
    if request.method == 'POST':
        your_data = request.POST.get('your_field')
        print("kys: ", your_data)
        return HttpResponse('Data received successfully.')
    return render(request, 'index.html')