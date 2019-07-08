from django.contrib import messages
from django.shortcuts import render, redirect
from .models import GetInTouch

# Create your views here.

def index(request):
    return redirect('en')
    

def en(request):
    
    if request.method == 'POST':
        
        posted_email = request.POST['email']
        
        # Check if email already in
        check_email = GetInTouch.objects.filter(email=posted_email)
        
        if check_email:
            messages.info(request, f'{posted_email} is already in touch with us. We\'ll give you a shout soon!')
        
        else:
            temp_email = GetInTouch.objects.create(email=posted_email, language="en")
            temp_email.save()
            messages.success(request, f'Hello {posted_email}! We\'ll get in touch with you very soon!')
        
        # Connext for English version
        context = {
            "lang": "en",
            "title": "Vars&Sava Devs - Coming Soon",
            "text1": "Greatness in the making",
            "text2": "Vars&Sava Devs are working hard on every little detail of our first website. Be sure to check us out in",
            "text3": "September 2019",
        }
        return render(request, 'website/index.html', context)
        
    else:
        context = {
            "lang": "en",
            "title": "Vars&Sava Devs - Coming Soon",
            "text1": "Greatness in the making",
            "text2": "Vars&Sava Devs are working hard on every little detail of our first website. Be sure to check us out in",
            "text3": "September 2019",
        }
        return render(request, 'website/index.html', context)
    
    
def pl(request):
    
    if request.method == 'POST':
        
        posted_email = request.POST['email']
        
        # Check if email already in
        check_email = GetInTouch.objects.filter(email=posted_email)
        
        if check_email:
            messages.info(request, f'{posted_email} już jest na naszej liście. Będziemy w kontakcie!')
        
        else:
            temp_email = GetInTouch.objects.create(email=posted_email, language="pl")
            temp_email.save()
            messages.success(request, f'Cześć {posted_email}! Wkrótce się odezwiemy!')
        
        # Context for Polish version
        context = {
            "lang": "pl",
            "title": "Vars&Sava Devs - Budujemy!",
            "text1": "Praca wre!", 
            "text2": "Para bucha w fabryce Vars&Sava Devs! Chuchamy i dmuchamy na nasz kod, żeby przywitać Was przepiekną stroną z naszym portfolio. Sprawdź efekt końcowy we",
            "text3": "wrzesniu 2019!",
        }
        return render(request, 'website/index.html', context)
    
    else:
        context = {
            "lang": "pl",
            "title": "Vars&Sava Devs - Budujemy!",
            "text1": "Praca wre!", 
            "text2": "Para bucha w fabryce Vars&Sava Devs! Chuchamy i dmuchamy na nasz kod, żeby przywitać Was przepiekną stroną z naszym portfolio. Sprawdź efekt końcowy we",
            "text3": "wrzesniu 2019!",
        }
        return render(request, 'website/index.html', context)